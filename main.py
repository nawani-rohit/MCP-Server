from fastapi import FastAPI, HTTPException, Query
from launch_data import fetch_launches
import analysis

app = FastAPI(title= "SpaceX MCP Server")

@app.get("/mcp/launches/analysis")
def analyze_launches(analysisType: str = Query(...)):
    launches = fetch_launches()

    if analysisType == "countByYear":
        return analysis.count_by_year(launches)
    
    if analysisType == "successVsFailure":
        return analysis.success_vs_failure(launches)
    
    if analysisType == "mostFrequentSite":
        results = analysis.most_frequent_site(launches)

        if not results:
            raise HTTPException(status_code=404, detail="No launch sites found")
    
        return results
    
    raise HTTPException(status_code=400, detail="Invalid analysis type")