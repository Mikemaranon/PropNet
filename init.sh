#!/bin/bash

structure=(
    "1_Business_Case_Discovery/business_case_description.md"
    "1_Business_Case_Discovery/stakeholder_requirements.md"
    "1_Business_Case_Discovery/success_metrics.md"
    
    "2_Data_Processing/correlation_analysis/01_correlation_analysis.ipynb"
    "2_Data_Processing/correlation_analysis/data_generation.py"
    "2_Data_Processing/feature_engineering/01_feature_engineering.ipynb"
    "2_Data_Processing/normalizing_data/03_normalizing_data.csv"
    
    "3_Model_Planning/model_definition.md"
    "3_Model_Planning/model_architecture.md"
    "3_Model_Planning/model_evaluation.md"
    
    "4_Model_Building_and_Selection/model.py"
    
    "5_Deployment/model_serialization.py"
    "5_Deployment/api_prediction.py"
    "5_Deployment/deployment_instructions.md"
    
    "requirements.txt"
)

for file in "${structure[@]}"; do
    mkdir -p "$(dirname "$file")"
    touch "$file"
done

echo "Project structure created :)"