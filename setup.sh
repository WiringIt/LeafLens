#mkdir -p ~/.streamlit/
#
#echo "\
#[server]\n\
#port=$PORT\n\
#enableCORS=false\n\
#headless=true\n\
#\n\
#"> ~/.streamlit/config.toml
# Install dependencies (optional if you're using requirements.txt)
pip install -r requirements.txt

# Create the `.streamlit` directory for Streamlit configuration
mkdir -p ~/.streamlit/

# Add Streamlit configuration
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml