#!/usr/bin/env python3
"""
Main Platform for Business Intelligence Capstone Project

This module serves as the entry point for the Business Intelligence platform,
integrating all components including data warehouse, ETL, OLAP, dashboards,
and reporting functionality.
"""

import os
import sys
import logging
import argparse
from datetime import datetime

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import platform components
from src.bi_platform import BusinessIntelligencePlatform

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('bi_platform.log')
    ]
)
logger = logging.getLogger(__name__)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Business Intelligence Platform')
    
    parser.add_argument('--mode', type=str, default='interactive',
                        choices=['interactive', 'etl', 'olap', 'dashboard', 'report'],
                        help='Operation mode')
    
    parser.add_argument('--etl', type=str, 
                        choices=['full', 'incremental'],
                        help='ETL operation type')
    
    parser.add_argument('--cube', type=str,
                        choices=['sales', 'inventory', 'finance', 'customer'],
                        help='OLAP cube to process')
    
    parser.add_argument('--dashboard', type=str,
                        choices=['executive', 'sales', 'finance', 'operations'],
                        help='Dashboard to generate')
    
    parser.add_argument('--report', type=str,
                        choices=['ceo', 'cfo', 'sales', 'operations'],
                        help='Report to generate')
    
    parser.add_argument('--output-dir', type=str, default='output',
                        help='Output directory for reports and dashboards')
    
    return parser.parse_args()

def run_interactive_mode():
    """Run the platform in interactive mode"""
    print("\n===== Business Intelligence Platform =====\n")
    print("1. Run ETL Process")
    print("2. Process OLAP Cubes")
    print("3. Generate Dashboards")
    print("4. Generate Reports")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        etl_type = input("ETL type (full/incremental): ").lower()
        if etl_type in ['full', 'incremental']:
            run_etl_process(etl_type)
        else:
            print("Invalid ETL type. Please enter 'full' or 'incremental'.")
    
    elif choice == '2':
        cube = input("Cube to process (sales/inventory/finance/customer/all): ").lower()
        if cube in ['sales', 'inventory', 'finance', 'customer', 'all']:
            process_olap_cubes(cube)
        else:
            print("Invalid cube selection.")
    
    elif choice == '3':
        dashboard = input("Dashboard to generate (executive/sales/finance/operations/all): ").lower()
        if dashboard in ['executive', 'sales', 'finance', 'operations', 'all']:
            generate_dashboards(dashboard)
        else:
            print("Invalid dashboard selection.")
    
    elif choice == '4':
        report = input("Report to generate (ceo/cfo/sales/operations/all): ").lower()
        if report in ['ceo', 'cfo', 'sales', 'operations', 'all']:
            generate_reports(report)
        else:
            print("Invalid report selection.")
    
    elif choice == '5':
        print("Exiting Business Intelligence Platform.")
        sys.exit(0)
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

def run_etl_process(etl_type):
    """Run the ETL process"""
    logger.info(f"Starting ETL process ({etl_type})...")
    
    try:
        # In a real implementation, this would import and use the ETL module
        # from src.etl.run_etl_pipeline import run_etl_pipeline
        # success = run_etl_pipeline(full_load=(etl_type == 'full'))
        
        # Simulate ETL process
        print(f"Running {etl_type} ETL process...")
        import time
        time.sleep(2)  # Simulate processing time
        success = True
        
        if success:
            logger.info("ETL process completed successfully.")
            print("ETL process completed successfully.")
        else:
            logger.error("ETL process failed.")
            print("ETL process failed. Check logs for details.")
    
    except Exception as e:
        logger.exception(f"Error in ETL process: {str(e)}")
        print(f"Error in ETL process: {str(e)}")

def process_olap_cubes(cube):
    """Process OLAP cubes"""
    logger.info(f"Processing OLAP cubes ({cube})...")
    
    try:
        # In a real implementation, this would import and use the OLAP module
        # from src.olap.refresh_cubes import OLAPCubeManager
        # cube_manager = OLAPCubeManager()
        # 
        # if cube == 'all':
        #     success = cube_manager.refresh_all_cubes()
        # else:
        #     success = cube_manager.refresh_cube(cube)
        
        # Simulate OLAP processing
        print(f"Processing OLAP cube(s): {cube}...")
        import time
        time.sleep(2)  # Simulate processing time
        success = True
        
        if success:
            logger.info("OLAP processing completed successfully.")
            print("OLAP processing completed successfully.")
        else:
            logger.error("OLAP processing failed.")
            print("OLAP processing failed. Check logs for details.")
    
    except Exception as e:
        logger.exception(f"Error in OLAP processing: {str(e)}")
        print(f"Error in OLAP processing: {str(e)}")

def generate_dashboards(dashboard):
    """Generate dashboards"""
    logger.info(f"Generating dashboards ({dashboard})...")
    
    try:
        # In a real implementation, this would import and use the dashboard module
        # from src.dashboards.dashboard_generator import DashboardGenerator
        # generator = DashboardGenerator()
        # 
        # if dashboard == 'all':
        #     success = generator.generate_all_dashboards()
        # else:
        #     success = generator.generate_dashboard(dashboard)
        
        # Simulate dashboard generation
        print(f"Generating dashboard(s): {dashboard}...")
        import time
        time.sleep(2)  # Simulate processing time
        success = True
        
        if success:
            logger.info("Dashboard generation completed successfully.")
            print("Dashboard generation completed successfully.")
        else:
            logger.error("Dashboard generation failed.")
            print("Dashboard generation failed. Check logs for details.")
    
    except Exception as e:
        logger.exception(f"Error in dashboard generation: {str(e)}")
        print(f"Error in dashboard generation: {str(e)}")

def generate_reports(report):
    """Generate reports"""
    logger.info(f"Generating reports ({report})...")
    
    try:
        # In a real implementation, this would import and use the reporting module
        # from src.reporting.generate_executive_reports import ExecutiveReportGenerator
        # generator = ExecutiveReportGenerator()
        # 
        # if report == 'all':
        #     results = generator.generate_all_reports()
        #     success = all(results.values())
        # else:
        #     success = generator.generate_report(report)
        
        # Simulate report generation
        print(f"Generating report(s): {report}...")
        import time
        time.sleep(2)  # Simulate processing time
        success = True
        
        if success:
            logger.info("Report generation completed successfully.")
            print("Report generation completed successfully.")
        else:
            logger.error("Report generation failed.")
            print("Report generation failed. Check logs for details.")
    
    except Exception as e:
        logger.exception(f"Error in report generation: {str(e)}")
        print(f"Error in report generation: {str(e)}")

def main():
    """Main function"""
    logger.info("Starting Business Intelligence Platform")
    
    args = parse_arguments()
    
    # Create platform instance
    platform = BusinessIntelligencePlatform()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Run in specified mode
    if args.mode == 'interactive':
        run_interactive_mode()
    elif args.mode == 'etl':
        if args.etl:
            run_etl_process(args.etl)
        else:
            logger.error("ETL type must be specified with --etl")
            sys.exit(1)
    elif args.mode == 'olap':
        if args.cube:
            process_olap_cubes(args.cube)
        else:
            logger.error("Cube must be specified with --cube")
            sys.exit(1)
    elif args.mode == 'dashboard':
        if args.dashboard:
            generate_dashboards(args.dashboard)
        else:
            logger.error("Dashboard must be specified with --dashboard")
            sys.exit(1)
    elif args.mode == 'report':
        if args.report:
            generate_reports(args.report)
        else:
            logger.error("Report must be specified with --report")
            sys.exit(1)

if __name__ == "__main__":
    main()
