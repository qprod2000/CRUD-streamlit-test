import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def main():
    st.title("CRUD Application")
    
    # Debug: Print environment variables (hide sensitive parts)
    st.write("Supabase URL:", os.getenv("SUPABASE_URL")[:20] + "...")
    
    try:
        # Try to list all tables
        response = supabase.table("items").select("*").execute()
        st.write("Success:", response)
    except Exception as e:
        st.write("Error:", str(e))
        st.write("Type of error:", type(e))

if __name__ == "__main__":
    main()