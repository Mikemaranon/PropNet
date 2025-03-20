#!/bin/bash

structure=(
    "1_Business_Case_Discovery/business_case_description.md"
    "1_Business_Case_Discovery/stakeholder_requirements.md"
    "1_Business_Case_Discovery/success_metrics.md"
    
    "2_Data_Processing/data_exploration/01_load_and_explore_data.ipynb"
    
    "2_Data_Processing/correlation_analysis/02_correlation_analysis.ipynb"
    
    "2_Data_Processing/data_preprocessing/03_preprocess_data.ipynb"
    "2_Data_Processing/data_preprocessing/feature_encoding.py"
    "2_Data_Processing/data_preprocessing/feature_scaling.py"
    "2_Data_Processing/data_preprocessing/train_test_split.py"
    
    "2_Data_Processing/processed_data/train_data.csv"
    "2_Data_Processing/processed_data/test_data.csv"
    "2_Data_Processing/processed_data/features_description.md"
    
    "3_Model_Planning/model_definition.md"
    "3_Model_Planning/model_architecture.md"
    "3_Model_Planning/loss_function_optimizer.md"
    "3_Model_Planning/model_evaluation.md"
    
    "4_Model_Building_and_Selection/model_architecture.py"
    "4_Model_Building_and_Selection/model_training.py"
    "4_Model_Building_and_Selection/hyperparameter_tuning.py"
    "4_Model_Building_and_Selection/model_validation.py"
    "4_Model_Building_and_Selection/model_performance.py"
    "4_Model_Building_and_Selection/model_comparison.py"
    
    "5_Results_Presentation/result_visualization.py"
    "5_Results_Presentation/error_analysis.py"
    "5_Results_Presentation/rmse_vs_r2_comparison.py"
    "5_Results_Presentation/final_report.md"
    
    "6_Deployment/model_serialization.py"
    "6_Deployment/api_prediction.py"
    "6_Deployment/deployment_instructions.md"
    
    "requirements.txt"
)

for file in "${structure[@]}"; do
    mkdir -p "$(dirname "$file")"
    touch "$file"
done

echo "Project structure created :)"