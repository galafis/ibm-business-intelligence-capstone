#!/usr/bin/env python3
"""Business Intelligence Platform"""
import pandas as pd
import sqlite3

class BusinessIntelligencePlatform:
    def __init__(self):
        self.connection = None
    
    def connect_database(self, db_path):
        self.connection = sqlite3.connect(db_path)
        return True
    
    def calculate_kpis(self, data):
        kpis = {
            'total_revenue': data['revenue'].sum(),
            'avg_revenue': data['revenue'].mean()
        }
        return kpis

if __name__ == "__main__":
    print("Business Intelligence Platform initialized")
