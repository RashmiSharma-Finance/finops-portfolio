"""
GenAI Token Economics & Operational Leverage Predictive Model
Description: Simulates corporate financial gross profit margins based on API token 
             consumption variations, cache hit rates, and input/output vector sizes.
"""
import pandas as pd
import io

def simulate_ai_infrastructure_margins(monthly_api_calls, input_tokens_per_call, output_tokens_per_call, cache_hit_rate=0.0):
    # Standard pricing metrics for an enterprise-tier LLM API engine
    cost_per_1k_input = 0.0015  # €0.0015 per 1,000 input tokens
    cost_per_1k_output = 0.0020 # €0.0020 per 1,000 output tokens
    
    # Fixed subscription SaaS revenue generated per transactional active customer
    revenue_per_call = 0.05    # €0.05 income allocated per processed query
    
    # Apply context cache hit discounts to input tokens
    effective_input_tokens = input_tokens_per_call * (1.0 - cache_hit_rate)
    
    # Compute underlying mathematical infrastructure cost vectors
    input_cost_total = (monthly_api_calls * effective_input_tokens / 1000) * cost_per_1k_input
    output_cost_total = (monthly_api_calls * output_tokens_per_call / 1000) * cost_per_1k_output
    total_infrastructure_cogs = input_cost_total + output_cost_total
    
    # Financial performance metrics
    gross_revenue = monthly_api_calls * revenue_per_call
    gross_profit = gross_revenue - total_infrastructure_cogs
    gross_margin_percentage = (gross_profit / gross_revenue) * 100
    
    return {
        "Volume": monthly_api_calls,
        "Total Revenue (€)": round(gross_revenue, 2),
        "Infra COGS (€)": round(total_infrastructure_cogs, 2),
        "Gross Profit (€)": round(gross_profit, 2),
        "Gross Margin (%)": round(gross_margin_percentage, 2)
    }

if __name__ == "__main__":
    print("=== STRATEGIC AI INFRASTRUCTURE CAPITAL FORECAST ===")
    
    # Scenario: Scalability forecast comparing un-cached calls vs highly optimized cache pipelines
    volumes = [10000, 100000, 500000]
    results_unoptimized = []
    results_optimized = []
    
    for v in volumes:
        results_unoptimized.append(simulate_ai_infrastructure_margins(v, 2000, 1000, cache_hit_rate=0.0))
        results_optimized.append(simulate_ai_infrastructure_margins(v, 2000, 1000, cache_hit_rate=0.40)) # 40% Semantic Cache Hit
        
    df_unopt = pd.DataFrame(results_unoptimized)
    df_opt = pd.DataFrame(results_optimized)
    
    print("\n[SCENARIO A] UNOPTIMIZED SYSTEM SCALING (0% Semantic Caching):")
    print(df_unopt.to_markdown(index=False))
    
    print("\n[SCENARIO B] OPTIMIZED SYSTEMS (40% Semantic Cache Hit Implemented via .NET Gateways):")
    print(df_opt.to_markdown(index=False))
    
    print("\nStrategic MBA Insight: Integrating structural semantic caching saves thousands in variable infrastructure COGS as application utilization increases, directly driving superior corporate operating leverage.")