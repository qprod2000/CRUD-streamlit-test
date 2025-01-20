# Update this part in your app.py
def main():
    st.title("CRUD Application")
    
    # Create
    with st.form("create_form"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        if st.form_submit_button("Create"):
            try:
                data = supabase.table("items").insert({
                    "title": title, 
                    "description": description
                }).execute()
                st.success("Item created!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    # Read
    try:
        items = supabase.table("items").select("*").execute()
        for item in items.data:
            with st.expander(f"Item: {item['title']}"):
                st.write(f"ID: {item['id']}")
                st.write(f"Description: {item['description']}")
                st.write(f"Created: {item['created_at']}")
                
                # Update
                if st.button(f"Edit {item['id']}"):
                    updated_title = st.text_input("New Title", item['title'])
                    updated_desc = st.text_area("New Description", item['description'])
                    if st.button("Update"):
                        supabase.table("items").update({
                            "title": updated_title,
                            "description": updated_desc
                        }).eq("id", item['id']).execute()
                        st.success("Item updated!")
                
                # Delete
                if st.button(f"Delete {item['id']}"):
                    supabase.table("items").delete().eq("id", item['id']).execute()
                    st.success("Item deleted!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()