#!/usr/bin/env python3
"""Data Extraction Module"""
import logging
import pandas as pd
import pyodbc
import requests
import json
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class DataExtractor:
    """Data Extractor class for retrieving data from various sources"""
    
    def __init__(self):
        self.connection_strings = {
            'sales': 'DRIVER={SQL Server};SERVER=sales-db;DATABASE=Sales;UID=etl_user;PWD=password',
            'inventory': 'DRIVER={SQL Server};SERVER=inventory-db;DATABASE=Inventory;UID=etl_user;PWD=password',
            'customers': 'DRIVER={SQL Server};SERVER=crm-db;DATABASE=CRM;UID=etl_user;PWD=password'
        }
        self.api_endpoints = {
            'products': 'https://api.company.com/products',
            'orders': 'https://api.company.com/orders'
        }
        self.file_paths = {
            'promotions': '/data/promotions.csv',
            'stores': '/data/stores.xlsx'
        }
    
    def extract_from_database(self, source, query=None, table=None, incremental=True):
        """Extract data from a database source"""
        try:
            conn = pyodbc.connect(self.connection_strings[source])
            
            if query:
                return pd.read_sql(query, conn)
            elif table:
                if incremental:
                    # Get last extraction date from metadata
                    last_extract = self._get_last_extraction_date(source, table)
                    query = f"SELECT * FROM {table} WHERE LastModified >= '{last_extract}'"
                else:
                    query = f"SELECT * FROM {table}"
                
                return pd.read_sql(query, conn)
            else:
                raise ValueError("Either query or table must be provided")
        
        except Exception as e:
            logger.error(f"Error extracting from database {source}: {str(e)}")
            raise
    
    def extract_from_api(self, endpoint, params=None):
        """Extract data from an API endpoint"""
        try:
            url = self.api_endpoints[endpoint]
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            return pd.DataFrame(response.json())
        
        except Exception as e:
            logger.error(f"Error extracting from API {endpoint}: {str(e)}")
            raise
    
    def extract_from_file(self, source):
        """Extract data from a file source"""
        try:
            file_path = self.file_paths[source]
            
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                return pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    return pd.DataFrame(json.load(f))
            else:
                raise ValueError(f"Unsupported file format: {file_path}")
        
        except Exception as e:
            logger.error(f"Error extracting from file {source}: {str(e)}")
            raise
    
    def extract_from_systems(self, systems):
        """Extract data from specified systems"""
        data = {}
        
        for system in systems:
            if system in self.connection_strings:
                data[system] = self.extract_from_database(system, table=system)
            elif system in self.api_endpoints:
                data[system] = self.extract_from_api(system)
            elif system in self.file_paths:
                data[system] = self.extract_from_file(system)
            else:
                logger.warning(f"Unknown system: {system}")
        
        return data
    
    def extract_all(self):
        """Extract data from all configured sources"""
        data = {}
        
        # Extract from databases
        for source in self.connection_strings:
            data[source] = self.extract_from_database(source, table=source)
        
        # Extract from APIs
        for endpoint in self.api_endpoints:
            data[endpoint] = self.extract_from_api(endpoint)
        
        # Extract from files
        for source in self.file_paths:
            data[source] = self.extract_from_file(source)
        
        return data
    
    def _get_last_extraction_date(self, source, table):
        """Get the last extraction date for incremental loads"""
        # In a real implementation, this would retrieve from a metadata table
        # For this example, we'll just return yesterday's date
        return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
