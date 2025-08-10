import streamlit as st
import sys
from pathlib import Path
# Add this before your other imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Now use either:
from utils.db import run_query
#from FinSightx.utils.db import run_query

st.title("📊 Company Dashboard")

company = st.text_input("Enter company name:")

if st.button("Load Data"):
    query = f"""
            SELECT  
    		fin.[PERIOD_ID],
    		fin.[VIEW_ID],
    		vw.VIEW_LABEL,
    		MAX(fin.[INSERT_DATE]) AS INSERT_DATE,
    		MAX(fin.[UPDATE_DATE]) As UPDATE_DATE
        FROM [CDR_DEV_WAREHOUSE].[ONEHFM].[ONEHFM_MAFPTB_F_FINANCIAL_FINAL] as fin
        LEFT JOIN [CDR_DEV_WAREHOUSE].[ONEHFM].[onehfm_mafptb_d_value] as val ON val.VALUE_ID = fin.VALUE_ID
        LEFT JOIN [CDR_DEV_WAREHOUSE].[ONEHFM].[onehfm_mafptb_d_view] as vw ON vw.VIEW_ID = fin.VIEW_ID
        WHERE PERIOD_ID IN (202507,202506,202505)	
        GROUP BY 	fin.[PERIOD_ID],
        			fin.[VIEW_ID],
        			vw.VIEW_LABEL
        ORDER BY 	fin.[PERIOD_ID],
        			fin.[VIEW_ID],
        			vw.VIEW_LABEL;"""
    df = run_query(query)
    st.dataframe(df)
