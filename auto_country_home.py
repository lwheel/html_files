import os
import pandas as pd

general_df = pd.read_excel("/Users/lilywheeler/Desktop/main_info.xlsx", engine="openpyxl")

for row_number, row in general_df.iterrows():
    # Extract the relevant information for the current row
    site_name = row['Site Name'].title()  # Capitalize the first letter of each word
    logo = row['Logo Link']
    acro = row['acronym']

# Read the Excel file
df = pd.read_excel("/Users/lilywheeler/Desktop/countries.xlsx", engine="openpyxl")

# Create the output directory if it doesn't exist
output_directory = "docs"
os.makedirs(output_directory, exist_ok=True)


# Iterate over each row in the DataFrame
for row_number, row in df.iterrows():
    # Extract the relevant information for the current row
    total_part = row['Number of Participants']
    men = row['Number of Men']
    women = row['Number of Women']
    gold_medal = row['Gold Medals']
    silver_medal = row['Silver Medals']
    bronze_medal = row['Bronze Medals']
    rank = row['Rank']

    # Generate the XML content for the student's webpage
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
    <link href="App_Themes/fav-logo.ico" rel="shortcut icon" type="image/x-icon" />
    <link href="App_Themes/design.css" rel="stylesheet" type="text/css" />
    <link href="App_Themes/print.css" rel="stylesheet" type="text/css" media="print" />
    <title>International Mathematical Olympiad</title>
    <style>
             @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
                 body {{
         font-family: "Poppins", sans-serif;
         background-color: #ffffff;
         margin: 0;
         margin: 40 px;
         padding: 0;
         overflow: auto;}}
   
       .container {{
         display: flex;
         flex-direction: column;
         min-height: 100vh;
       }}
   
       .content {{
         flex: 1;
         padding: 2rem;
         margin-left: 20%;
       }}
   
       .centered-heading {{
         font-family: "Poppins", sans-serif;
         margin: 0;
         padding: 0;
         overflow: auto;
         text-align: center;
         font-weight: 700;
         font-size: 50px;
     
       }}
   
       .centered-image {{
         display: flex;
         justify-content: center;
         margin-top: 1rem;
       }}
   
       #header {{
         background-color: #ffffff;
         padding: 2rem;
       }}
   
       .top-left-corner {{
         position: absolute;
         top: 14px;
         left: 12px;
       }}
   
       #menu {{
         font-family: "Poppins", "sans-serif";
         display: flex;
         justify-content: center;
         margin-top: 1rem;
         color: #000000;
         font-size: 1.2rem;
         font-weight: 700;
       }}
   
       #menu a {{
         margin: 0 1rem;
         text-decoration: none;
         color: #000000;
         transition: color 0.3s ease-in-out;
       }}
   
       #menu a:hover {{
         color: #4B86DB;
       }}
   
       footer {{
      background-image: url('https://lwheel.github.io/FILESMO/repeat1.png');
      background-size: contain;
      background-repeat: repeat;
      color: rgb(0, 0, 0);
      text-align: left;
      font-size: 12px; /* Decreased font size */
      line-height: 1em;
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      padding: 0.2em 2em; /* Decreased padding */
      box-sizing: border-box;
      margin: 0;
      z-index: 5;
      text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
  }}

  footer::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(255, 255, 255, 0.2);
      z-index: -1;
  }}

  footer b {{
      font-size: 10px;
      margin-top: auto;
  }}

  footer a {{
      color: rgb(0, 0, 0);
      font-size: 10px;
  }}

     #main {{
         margin-left: 30px; /* Adjust this value to move the content further to the right */
    }}

   
       header,
       h1 {{
         font-family: "Poppins", sans-serif;
         font-size: 30px;
         font-weight: 700;
         color: #000000;
         margin-bottom: 2rem;
       }}
       #h1 a{{
         text-decoration: none;
         color: #000000;
         transition: color 0.3s ease-in-out;
       }}
       #h1 a:hover {{
         color: #4B86DB;
       }}
       .intro {{
         text-align: left;
         margin-left: 1000 px;
         margin-right: 1000 px;
       }}
   
       /* Media Queries */
       @media screen and (max-width: 768px) {{
         .centered-heading {{
           font-size: 1.8rem;
         }}
   
         header,
         h1 {{
           font-size: 50px;
         }}
       }}
table {{
        border-collapse: collapse;
        width: 50%;
    }}
    
    th, td {{
        border: 1px solid black;
        padding: 2px;
        text-align: center;
    }}
    
    tr:nth-child(even) {{
        background-color: #f2f2f2;
    }}
    
    .highlightDown {{
        border-bottom: 2px solid black;
    }}
    
    .imp {{
        font-weight: bold;
    }}
    </style>
</head>
<body>
     <div id="header">
        <div id="sub">
          <div class="centered-image top-left-corner">
            <a href="index.html">
              <img src="{logo}" alt="EAMO" style="width: 100px; height: 77px;">
            </a>
          </div>
        </div>
    
        <div id="h1">
          <h1 class="centered-heading">
            <a href="index.html">{site_name}</a>
          </h1>
        </div>
        <div id="menu">
          <a href="about.html">About {acro}</a> &bull;
          <a href="results.html">Results</a> &bull;
          <a href="problems.html">Problems</a> &bull;
          <a href="links.html">Links and Resources</a>
        </div>
      </div><hr>
    <div id="main">
<h2>Results</h2>
<h3 class="hideprn"><a id="ctl00_CPH_Main_HyperLinkTeam" href="team_results.html">Team results</a> &bull;
<a id="ctl00_CPH_Main_HyperLinkIndividual" href="hall.html">Individual results</a> 

<dl class="normal">



</dd><dd>Number of participations: {total_part}.</dd><dd>Gold medals: {gold_medal}. Silver medals: {silver_medal}. Bronze medals: {bronze_medal}.</dd>
</dl>






  <footer>
    <b>E-mail:</b>
    <a href="mailto:">__</a>
    &nbsp; &nbsp;
    <br>  
    <b>Webmaster:</b>
    <a href="mailto:ea@globtalent.org">ea@globtalent.org</a>
  </footer>
</body>
</html>
'''

    # Save the XML content to a file in the output directory
    output_filename = os.path.join(output_directory, f"results.html")
    with open(output_filename, "w") as file:
        file.write(xml_content)
