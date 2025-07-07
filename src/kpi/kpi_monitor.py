#!/usr/bin/env python3
"""KPI Monitoring Module"""
import argparse
import logging
import sys
import time
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KPIMonitor:
    """KPI Monitor for tracking and alerting on business KPIs"""
    
    def __init__(self, db_path=':memory:'):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.kpis = {
            'revenue': {
                'name': 'Total Revenue',
                'query': 'SELECT SUM(SalesAmount) FROM FactSales WHERE DateKey >= ?',
                'threshold': 100000,
                'comparison': '>',
                'period': 'daily',
                'alert_level': 'high'
            },
            'new_customers': {
                'name': 'New Customers',
                'query': 'SELECT COUNT(*) FROM DimCustomer WHERE StartDate >= ?',
                'threshold': 50,
                'comparison': '>',
                'period': 'daily',
                'alert_level': 'medium'
            },
            'inventory_turnover': {
                'name': 'Inventory Turnover',
                'query': '''
                    SELECT SUM(s.Quantity) / AVG(i.QuantityOnHand)
                    FROM FactSales s
                    JOIN FactInventory i ON s.ProductKey = i.ProductKey
                    WHERE s.DateKey >= ?
                ''',
                'threshold': 2.0,
                'comparison': '>',
                'period': 'monthly',
                'alert_level': 'medium'
            },
            'profit_margin': {
                'name': 'Profit Margin',
                'query': '''
                    SELECT SUM(Profit) / SUM(SalesAmount) * 100
                    FROM FactSales
                    WHERE DateKey >= ?
                ''',
                'threshold': 15.0,
                'comparison': '>',
                'period': 'weekly',
                'alert_level': 'high'
            }
        }
    
    def calculate_kpi(self, kpi_id, as_of_date=None):
        """Calculate a specific KPI value"""
        if kpi_id not in self.kpis:
            logger.error(f"KPI {kpi_id} not found")
            return None
        
        kpi = self.kpis[kpi_id]
        
        if as_of_date is None:
            as_of_date = datetime.now()
        
        # Calculate period start date
        if kpi['period'] == 'daily':
            period_start = as_of_date.replace(hour=0, minute=0, second=0, microsecond=0)
        elif kpi['period'] == 'weekly':
            period_start = as_of_date - timedelta(days=as_of_date.weekday())
            period_start = period_start.replace(hour=0, minute=0, second=0, microsecond=0)
        elif kpi['period'] == 'monthly':
            period_start = as_of_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            logger.error(f"Unknown period type: {kpi['period']}")
            return None
        
        try:
            # In a real implementation, this would connect to the actual data warehouse
            # For this example, we'll simulate the result
            # cursor = self.conn.cursor()
            # cursor.execute(kpi['query'], (period_start.strftime('%Y%m%d'),))
            # value = cursor.fetchone()[0]
            
            # Simulate KPI values
            import random
            if kpi_id == 'revenue':
                value = random.uniform(90000, 110000)
            elif kpi_id == 'new_customers':
                value = random.randint(40, 60)
            elif kpi_id == 'inventory_turnover':
                value = random.uniform(1.8, 2.2)
            elif kpi_id == 'profit_margin':
                value = random.uniform(14.0, 16.0)
            else:
                value = 0
            
            return {
                'kpi_id': kpi_id,
                'name': kpi['name'],
                'value': value,
                'threshold': kpi['threshold'],
                'comparison': kpi['comparison'],
                'period': kpi['period'],
                'period_start': period_start.strftime('%Y-%m-%d'),
                'as_of_date': as_of_date.strftime('%Y-%m-%d %H:%M:%S'),
                'status': self._evaluate_status(value, kpi['threshold'], kpi['comparison'])
            }
        
        except Exception as e:
            logger.error(f"Error calculating KPI {kpi_id}: {str(e)}")
            return None
    
    def calculate_all_kpis(self, as_of_date=None):
        """Calculate all KPIs"""
        results = {}
        
        for kpi_id in self.kpis:
            results[kpi_id] = self.calculate_kpi(kpi_id, as_of_date)
        
        return results
    
    def monitor_kpis_real_time(self, interval_seconds=60):
        """Monitor KPIs in real-time with specified interval"""
        logger.info(f"Starting real-time KPI monitoring (interval: {interval_seconds}s)")
        
        try:
            while True:
                logger.info("Calculating KPIs...")
                kpi_results = self.calculate_all_kpis()
                
                # Check for alerts
                alerts = []
                for kpi_id, result in kpi_results.items():
                    if result and result['status'] != 'normal':
                        alerts.append(result)
                
                # Display results
                self._display_kpi_results(kpi_results)
                
                # Handle alerts
                if alerts:
                    self._handle_alerts(alerts)
                
                # Store results
                self._store_kpi_results(kpi_results)
                
                logger.info(f"Waiting {interval_seconds} seconds until next check...")
                time.sleep(interval_seconds)
        
        except KeyboardInterrupt:
            logger.info("KPI monitoring stopped by user")
        except Exception as e:
            logger.error(f"Error in KPI monitoring: {str(e)}")
    
    def _evaluate_status(self, value, threshold, comparison):
        """Evaluate KPI status based on threshold and comparison"""
        if comparison == '>':
            if value > threshold * 1.1:
                return 'excellent'
            elif value > threshold:
                return 'good'
            elif value > threshold * 0.9:
                return 'warning'
            else:
                return 'critical'
        elif comparison == '<':
            if value < threshold * 0.9:
                return 'excellent'
            elif value < threshold:
                return 'good'
            elif value < threshold * 1.1:
                return 'warning'
            else:
                return 'critical'
        else:
            return 'unknown'
    
    def _display_kpi_results(self, results):
        """Display KPI results in a formatted way"""
        logger.info("KPI RESULTS:")
        logger.info("-" * 80)
        
        for kpi_id, result in results.items():
            if result:
                status_indicator = {
                    'excellent': '🟢',
                    'good': '🟢',
                    'warning': '🟠',
                    'critical': '🔴',
                    'unknown': '⚪'
                }.get(result['status'], '⚪')
                
                logger.info(f"{status_indicator} {result['name']}: {result['value']:.2f} (Threshold: {result['threshold']} {result['comparison']})")
        
        logger.info("-" * 80)
    
    def _handle_alerts(self, alerts):
        """Handle KPI alerts"""
        logger.warning(f"ALERTS: {len(alerts)} KPIs require attention")
        
        for alert in alerts:
            logger.warning(f"⚠️ {alert['name']} is {alert['status'].upper()}: {alert['value']:.2f} vs threshold {alert['threshold']} {alert['comparison']}")
            
            # In a real implementation, this would send emails, SMS, or other notifications
            # based on the alert_level of the KPI
    
    def _store_kpi_results(self, results):
        """Store KPI results for historical tracking"""
        # In a real implementation, this would store to a database
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"Stored KPI results at {timestamp}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Monitor Business KPIs')
    parser.add_argument('--real-time', action='store_true', help='Monitor KPIs in real-time')
    parser.add_argument('--interval', type=int, default=60, help='Interval in seconds for real-time monitoring')
    parser.add_argument('--kpi', type=str, help='Specific KPI to calculate')
    
    args = parser.parse_args()
    
    monitor = KPIMonitor()
    
    if args.real_time:
        monitor.monitor_kpis_real_time(args.interval)
    elif args.kpi:
        result = monitor.calculate_kpi(args.kpi)
        if result:
            print(f"{result['name']}: {result['value']}")
        else:
            print(f"Error calculating KPI: {args.kpi}")
            sys.exit(1)
    else:
        results = monitor.calculate_all_kpis()
        for kpi_id, result in results.items():
            if result:
                print(f"{result['name']}: {result['value']}")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
