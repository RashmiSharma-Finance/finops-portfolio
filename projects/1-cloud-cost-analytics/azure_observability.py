import pandas as pd
import io

def generate_mock_azure_billing_data():
    # Simulating a raw, messy Azure enterprise billing CSV export
    csv_data = """Timestamp,Subscription,ResourceGroup,MeterCategory,ResourceId,Cost,Tag_OwnerTeam
2026-06-01,Prod-Fintech-Sub,App-Layer-RG,Virtual Machines,vm-prod-dotnet-01,120.50,Web-Core-Squad
2026-06-01,Prod-Fintech-Sub,Data-Layer-RG,Azure SQL Database,sql-prod-db-01,450.00,Data-AI-Team
2026-06-02,Prod-Fintech-Sub,App-Layer-RG,Virtual Machines,vm-prod-dotnet-01,120.50,Web-Core-Squad
2026-06-02,Prod-Fintech-Sub,Experimental-RG,AI Service,ai-gpu-node-orphan,890.00,
2026-06-03,Staging-Sub,Test-RG,AKS,aks-cluster-node,45.00,DevOps-Infra
2026-06-03,Prod-Fintech-Sub,Experimental-RG,AI Service,ai-gpu-node-orphan,890.00,
"""
    return pd.read_csv(io.StringIO(csv_data))

def map_to_focus_schema(raw_df):
    """Maps custom cloud naming conventions to standard FOCUS column schemas"""
    focus_mapped = pd.DataFrame()
    focus_mapped['ChargePeriodStart'] = pd.to_datetime(raw_df['Timestamp'])
    focus_mapped['ProviderName'] = 'Microsoft'
    focus_mapped['SubAccountId'] = raw_df['Subscription']
    focus_mapped['ResourceGroup'] = raw_df['ResourceGroup']
    focus_mapped['ServiceCategory'] = raw_df['MeterCategory']
    focus_mapped['ResourceId'] = raw_df['ResourceId']
    focus_mapped['BilledCost'] = raw_df['Cost'].astype(float)
    focus_mapped['Tag_OwnerTeam'] = raw_df['Tag_OwnerTeam'].fillna('UNALLOCATED')
    return focus_mapped

def analyze_cost_distribution(focus_df):
    print("=== FINOPS RISK ASSESSMENT REPORT ===")
    
    # 1. Calculate the 'Who': Spend by Engineering Team
    team_spend = focus_df.groupby('Tag_OwnerTeam')['BilledCost'].sum().reset_index()
    print("\n[1] TOTAL ACCRUED COST BY OPERATIONAL ENGINEERING TEAM:")
    print(team_spend.to_markdown(index=False))
    
    # 2. Isolate Leakages: High cost anomalies with missing ownership tags
    leaks = focus_df[(focus_df['Tag_OwnerTeam'] == 'UNALLOCATED') & (focus_df['BilledCost'] > 100)]
    if not leaks.empty:
        print("\nALERT: UNALLOCATED HIGH-COST INFRASTRUCTURE ANOMALIES DETECTED:")
        print(leaks[['ResourceId', 'ResourceGroup', 'BilledCost']].to_markdown(index=False))
        print("\nAction Required: Enforce compliance policies on these resource groups immediately to salvage gross profit margins.")

if __name__ == "__main__":
    raw_billing = generate_mock_azure_billing_data()
    focus_compliant_data = map_to_focus_schema(raw_billing)
    analyze_cost_distribution(focus_compliant_data)