#!/usr/bin/env python3
"""ETL Pipeline Runner"""
import argparse
import logging
import sys
import os

from extraction import DataExtractor
from transformation import DataTransformer
from loading import DataLoader
from data_quality import DataQualityChecker

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_etl_pipeline(full_load=False, source_systems=None, target_tables=None):
    """Run the ETL pipeline"""
    logger.info("Starting ETL pipeline")
    logger.info(f"Full load: {full_load}")
    
    try:
        # Initialize components
        extractor = DataExtractor()
        transformer = DataTransformer()
        loader = DataLoader()
        dq_checker = DataQualityChecker()
        
        # Extract data
        logger.info("Extracting data...")
        if source_systems:
            raw_data = extractor.extract_from_systems(source_systems)
        else:
            raw_data = extractor.extract_all()
        
        # Transform data
        logger.info("Transforming data...")
        transformed_data = transformer.transform(raw_data)
        
        # Check data quality
        logger.info("Checking data quality...")
        quality_results = dq_checker.check_quality(transformed_data)
        if not quality_results['passed']:
            logger.error(f"Data quality check failed: {quality_results['issues']}")
            return False
        
        # Load data
        logger.info("Loading data...")
        if target_tables:
            load_result = loader.load_to_tables(transformed_data, target_tables, full_load)
        else:
            load_result = loader.load_all(transformed_data, full_load)
        
        logger.info("ETL pipeline completed successfully")
        return load_result
    
    except Exception as e:
        logger.error(f"ETL pipeline failed: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run ETL Pipeline')
    parser.add_argument('--full-load', action='store_true', help='Perform full load instead of incremental')
    parser.add_argument('--source', nargs='+', help='Source systems to extract from')
    parser.add_argument('--target', nargs='+', help='Target tables to load into')
    
    args = parser.parse_args()
    
    success = run_etl_pipeline(
        full_load=args.full_load,
        source_systems=args.source,
        target_tables=args.target
    )
    
    sys.exit(0 if success else 1)
