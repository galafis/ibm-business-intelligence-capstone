#!/usr/bin/env python3
"""Executive Report Generator"""
import argparse
import logging
import sys
import os
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ExecutiveReportGenerator:
    """Executive Report Generator for creating business reports"""
    
    def __init__(self, output_dir='reports'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        self.reports = {
            'ceo': {
                'name': 'CEO Executive Dashboard',
                'sections': ['company_overview', 'financial_summary', 'strategic_initiatives', 'market_analysis'],
                'format': 'pdf'
            },
            'cfo': {
                'name': 'Financial Performance Report',
                'sections': ['revenue_analysis', 'expense_analysis', 'profit_margins', 'cash_flow'],
                'format': 'pdf'
            },
            'sales': {
                'name': 'Sales Performance Report',
                'sections': ['sales_by_region', 'sales_by_product', 'customer_acquisition', 'sales_forecast'],
                'format': 'pdf'
            },
            'operations': {
                'name': 'Operations Efficiency Report',
                'sections': ['inventory_levels', 'supply_chain', 'production_efficiency', 'quality_metrics'],
                'format': 'pdf'
            }
        }
    
    def generate_report(self, report_id, as_of_date=None, email=False):
        """Generate a specific executive report"""
        if report_id not in self.reports:
            logger.error(f"Report {report_id} not found")
            return False
        
        report = self.reports[report_id]
        
        if as_of_date is None:
            as_of_date = datetime.now()
        
        logger.info(f"Generating {report['name']} as of {as_of_date.strftime('%Y-%m-%d')}")
        
        try:
            # Create report sections
            sections = {}
            for section_id in report['sections']:
                sections[section_id] = self._generate_section(section_id, as_of_date)
            
            # Compile report
            report_path = self._compile_report(report_id, report, sections, as_of_date)
            
            if email and report_path:
                self._email_report(report_path, report_id, as_of_date)
            
            logger.info(f"Report generated successfully: {report_path}")
            return report_path
        
        except Exception as e:
            logger.error(f"Error generating report {report_id}: {str(e)}")
            return False
    
    def generate_all_reports(self, as_of_date=None, email=False):
        """Generate all executive reports"""
        results = {}
        
        for report_id in self.reports:
            results[report_id] = self.generate_report(report_id, as_of_date, email)
        
        success_count = sum(1 for result in results.values() if result)
        total_count = len(results)
        
        logger.info(f"Generated {success_count}/{total_count} reports successfully")
        
        return results
    
    def _generate_section(self, section_id, as_of_date):
        """Generate a specific report section"""
        logger.info(f"Generating section: {section_id}")
        
        # In a real implementation, this would query the data warehouse
        # and generate actual visualizations and content
        
        # Simulate data for different sections
        if section_id in ['company_overview', 'financial_summary', 'revenue_analysis', 'profit_margins']:
            # Financial data
            months = pd.date_range(end=as_of_date, periods=12, freq='M').strftime('%b %Y').tolist()
            revenue = [round(x * 1000) for x in [120, 132, 145, 135, 150, 178, 165, 188, 195, 210, 220, 240]]
            expenses = [round(x * 1000) for x in [100, 110, 115, 120, 125, 140, 135, 150, 155, 165, 170, 180]]
            profit = [r - e for r, e in zip(revenue, expenses)]
            
            df = pd.DataFrame({
                'Month': months,
                'Revenue': revenue,
                'Expenses': expenses,
                'Profit': profit
            })
            
            # Create visualization
            plt.figure(figsize=(10, 6))
            plt.plot(df['Month'], df['Revenue'], marker='o', label='Revenue')
            plt.plot(df['Month'], df['Expenses'], marker='s', label='Expenses')
            plt.plot(df['Month'], df['Profit'], marker='^', label='Profit')
            plt.title(f'Financial Performance - {section_id.replace("_", " ").title()}')
            plt.xlabel('Month')
            plt.ylabel('Amount ($)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            
            # Save visualization
            img_path = os.path.join(self.output_dir, f'{section_id}_{as_of_date.strftime("%Y%m%d")}.png')
            plt.savefig(img_path)
            plt.close()
            
            return {
                'title': section_id.replace('_', ' ').title(),
                'data': df,
                'visualization': img_path,
                'summary': f"This section shows the {section_id.replace('_', ' ')} for the past 12 months."
            }
        
        elif section_id in ['sales_by_region', 'sales_by_product', 'market_analysis']:
            # Sales data
            categories = ['North America', 'Europe', 'Asia', 'Latin America', 'Africa'] if 'region' in section_id else ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
            values = [round(x * 1000) for x in [240, 180, 160, 120, 80]]
            growth = [15, 8, 22, 5, 10]
            
            df = pd.DataFrame({
                'Category': categories,
                'Sales': values,
                'Growth': growth
            })
            
            # Create visualization
            plt.figure(figsize=(10, 6))
            ax = sns.barplot(x='Category', y='Sales', data=df)
            plt.title(f'Sales Analysis - {section_id.replace("_", " ").title()}')
            plt.xlabel('Category')
            plt.ylabel('Sales ($)')
            plt.xticks(rotation=45)
            
            # Add growth labels
            for i, p in enumerate(ax.patches):
                ax.annotate(f"{growth[i]}%", 
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha = 'center', va = 'center',
                            xytext = (0, 10),
                            textcoords = 'offset points')
            
            plt.tight_layout()
            
            # Save visualization
            img_path = os.path.join(self.output_dir, f'{section_id}_{as_of_date.strftime("%Y%m%d")}.png')
            plt.savefig(img_path)
            plt.close()
            
            return {
                'title': section_id.replace('_', ' ').title(),
                'data': df,
                'visualization': img_path,
                'summary': f"This section shows the {section_id.replace('_', ' ')} with growth percentages."
            }
        
        else:
            # Generic section
            return {
                'title': section_id.replace('_', ' ').title(),
                'summary': f"This section contains information about {section_id.replace('_', ' ')}."
            }
    
    def _compile_report(self, report_id, report, sections, as_of_date):
        """Compile report sections into a complete report"""
        if report['format'] == 'pdf':
            return self._compile_pdf_report(report_id, report, sections, as_of_date)
        else:
            logger.error(f"Unsupported report format: {report['format']}")
            return False
    
    def _compile_pdf_report(self, report_id, report, sections, as_of_date):
        """Compile a PDF report"""
        try:
            pdf = FPDF()
            
            # Add cover page
            pdf.add_page()
            pdf.set_font('Arial', 'B', 24)
            pdf.cell(0, 20, report['name'], 0, 1, 'C')
            pdf.set_font('Arial', '', 14)
            pdf.cell(0, 10, f"Generated on {as_of_date.strftime('%B %d, %Y')}", 0, 1, 'C')
            pdf.cell(0, 10, "CONFIDENTIAL", 0, 1, 'C')
            
            # Add table of contents
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, "Table of Contents", 0, 1, 'L')
            pdf.set_font('Arial', '', 12)
            
            for i, section_id in enumerate(report['sections']):
                if section_id in sections:
                    section = sections[section_id]
                    pdf.cell(0, 10, f"{i+1}. {section['title']}", 0, 1, 'L')
            
            # Add sections
            for section_id in report['sections']:
                if section_id in sections:
                    section = sections[section_id]
                    pdf.add_page()
                    
                    # Section title
                    pdf.set_font('Arial', 'B', 16)
                    pdf.cell(0, 10, section['title'], 0, 1, 'L')
                    
                    # Section summary
                    if 'summary' in section:
                        pdf.set_font('Arial', '', 12)
                        pdf.multi_cell(0, 10, section['summary'])
                    
                    # Section visualization
                    if 'visualization' in section and os.path.exists(section['visualization']):
                        pdf.image(section['visualization'], x=10, y=pdf.get_y() + 10, w=180)
                        pdf.ln(140)  # Space for the image
                    
                    # Section data table
                    if 'data' in section and isinstance(section['data'], pd.DataFrame):
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(0, 10, "Data Summary", 0, 1, 'L')
                        
                        df = section['data']
                        pdf.set_font('Arial', 'B', 10)
                        
                        # Table header
                        col_width = 180 / len(df.columns)
                        for col in df.columns:
                            pdf.cell(col_width, 10, str(col), 1, 0, 'C')
                        pdf.ln()
                        
                        # Table data
                        pdf.set_font('Arial', '', 10)
                        for _, row in df.head(5).iterrows():  # Show only first 5 rows
                            for item in row:
                                pdf.cell(col_width, 10, str(item), 1, 0, 'C')
                            pdf.ln()
            
            # Save the PDF
            output_path = os.path.join(self.output_dir, f"{report_id}_{as_of_date.strftime('%Y%m%d')}.pdf")
            pdf.output(output_path)
            
            return output_path
        
        except Exception as e:
            logger.error(f"Error compiling PDF report: {str(e)}")
            return False
    
    def _email_report(self, report_path, report_id, as_of_date):
        """Email the generated report"""
        # In a real implementation, this would use SMTP to send the email
        logger.info(f"Emailing report {report_path} to recipients")
        
        # Simulate email sending
        recipients = {
            'ceo': ['ceo@company.com'],
            'cfo': ['cfo@company.com', 'finance-team@company.com'],
            'sales': ['sales-director@company.com', 'regional-managers@company.com'],
            'operations': ['operations-director@company.com', 'plant-managers@company.com']
        }
        
        if report_id in recipients:
            for recipient in recipients[report_id]:
                logger.info(f"Sent report to {recipient}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Generate Executive Reports')
    parser.add_argument('--all', action='store_true', help='Generate all reports')
    parser.add_argument('--report', type=str, help='Specific report to generate')
    parser.add_argument('--email', action='store_true', help='Email reports after generation')
    parser.add_argument('--output-dir', type=str, default='reports', help='Output directory for reports')
    
    args = parser.parse_args()
    
    generator = ExecutiveReportGenerator(output_dir=args.output_dir)
    
    if args.all:
        results = generator.generate_all_reports(email=args.email)
        success = all(results.values())
    elif args.report:
        result = generator.generate_report(args.report, email=args.email)
        success = bool(result)
        if result:
            print(f"Report generated: {result}")
    else:
        logger.error("Either --all or --report must be specified")
        sys.exit(1)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
