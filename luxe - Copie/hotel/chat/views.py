# Import necessary libraries
import os
import imageio
import pandas as pd
from django.shortcuts import render, redirect
import openai
import os
import pandas as pd
from collections import Counter
from django.shortcuts import render
from django.http import JsonResponse
import os
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from django.shortcuts import render
from django.templatetags.static import static  # Import static for handling static files
import io
from django.http import HttpResponse 
import base64

from PIL import Image
from io import BytesIO
from django.conf import settings

import spacy

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Set your API key (use environment variables for security)
openai.api_key = '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'

# Define the path to the CSV file for hotels
csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

# Read the CSV file into a DataFrame for hotels
df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

# Function to generate an image using OpenAI GPT-3
# Modify the generate_image function to load an image from the 'data' folder

def showimages1(request):
    # Define the path to your image file
    html_image1 = 1
    return html_image1

def showimages2(request):
    # Define the path to your image file
    html_image2 = 1
    return html_image2

def showimages3(request):
    # Define the path to your image file
    html_image3 = 1
    return html_image3

def showppt(request):
    # Define the directory where your PowerPoint files are located
    ppt_directory = os.path.join(settings.MEDIA_ROOT, 'powerpoints')

    # Get a list of all PowerPoint files in the directory
    ppt_files = [os.path.join('media', 'powerpoints', f) for f in os.listdir(ppt_directory) if f.endswith('.pptx')]

    return ppt_files

def render_selected_plots():
    # Load the dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'travel trends.csv')
    df = pd.read_csv(csv_file_path)

    # Create a line chart to visualize the total number of travelers over the years
    fig = px.line(df, x='Year', y='Travelers (Millions)',
                  title='Travelers Over Time',
                  labels={'Year': 'Year', 'Travelers (Millions)': 'Total Travelers (Millions)'})

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html



def render_gender_distribution_chart():
    # Load your dataset (adjust the path)
    csv_file_path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

   # Read the CSV file into a DataFrame for hotels
    df1 = pd.read_csv(csv_file_path1, encoding='iso-8859-2')
    

    # Group the data by gender and count the number of guests in each category
    gender_distribution = df1['Gender'].value_counts()

    # Create a pie chart using Plotly Express
    
    fig1 = px.pie(gender_distribution, names=gender_distribution.index, title='Gender Distribution of Guests')

    # Customize the layout (optional)
    fig1.update_traces(textinfo='percent+label', pull=[0.1, 0], marker=dict(line=dict(color='#000000', width=2)))

    # Convert the chart to HTML
    chart_html1 = fig1.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html1







def render_travel_purpose_analysis():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Group the data by Travel_Purpose and count the number of guests in each category
    travel_purpose_counts = df['Travel_Purpose'].value_counts()

    # Create a bar chart using Plotly Express
    fig = px.bar(travel_purpose_counts, x=travel_purpose_counts.index, y=travel_purpose_counts.values,
                 title='Travel Purpose Analysis',
                 labels={'x': 'Travel Purpose', 'y': 'Number of Guests'})

    # Customize the layout (optional)
    fig.update_xaxes(title_text='Travel Purpose', tickangle=45)
    fig.update_yaxes(title_text='Number of Guests')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html



def render_loyalty_membership_analysis():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Group the data by loyalty membership and calculate the average revenue for each group
    loyalty_analysis = df.groupby('Loyalty_Membership')['Total_Revenue_usd'].mean().reset_index()

    # Create a bar chart using Plotly Express with different colors for each group
    fig = px.bar(loyalty_analysis, x='Loyalty_Membership', y='Total_Revenue_usd',
                 title='Loyalty Membership Analysis',
                 labels={'Loyalty_Membership': 'Loyalty Membership', 'Total_Revenue_usd': 'Average Revenue (USD)'},
                 color='Loyalty_Membership')

    # Customize the layout (optional)
    fig.update_layout(xaxis_categoryorder='total descending')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html





def stay_charts():
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Length of Stay Analysis Chart
    stay_fig = px.bar(df, x='Length_of_Stay', y='Total_Revenue_usd', title='Length of Stay Analysis', labels={'Length_of_Stay': 'Length of Stay (Days)', 'Total_Revenue_usd': 'Total Revenue (USD)'}, color='Length_of_Stay')
    chart_html = stay_fig.to_html(full_html=False, include_plotlyjs='cdn')

    return  chart_html



def render_source_of_booking_analysis():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Group the data by source of booking and calculate the total revenue for each source
    source_revenue = df.groupby('Source_of_Booking')['Total_Revenue_usd'].sum().reset_index()

    # Sort the data in descending order by total revenue
    source_revenue = source_revenue.sort_values(by='Total_Revenue_usd', ascending=False)

    # Create a bar chart using Plotly Express
    fig = px.bar(
        source_revenue,
        x='Total_Revenue_usd',
        y='Source_of_Booking',
        orientation='h',
        color='Source_of_Booking',
        labels={'Total_Revenue_usd': 'Total Revenue (USD)', 'Source_of_Booking': 'Booking Source'},
        title='Source of Booking Analysis'
    )

    # Customize the layout (optional)
    fig.update_layout(xaxis_title='Total Revenue (USD)', yaxis_title='Booking Source')
    fig.update_traces(marker_line_color='black', opacity=0.7)

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html


def render_room_type_distribution_chart():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Total Revenue by Room Type Chart
    room_type_distribution = df.groupby('Room_Type')['Total_Revenue_usd'].sum().reset_index()
    room_type_fig = px.bar(room_type_distribution, x='Room_Type', y='Total_Revenue_usd', title='Total Revenue by Room Type', labels={'Room_Type': 'Room Type', 'Total_Revenue_usd': 'Total Revenue (USD)'})

    # Customize the layout (optional)
    room_type_fig.update_traces(marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
                                marker_line_color='#000000', marker_line_width=2)

    # Customize the legend
    room_type_fig.update_layout(legend_title_text='Room Type')

    # Convert the chart to HTML
    chart_html = room_type_fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html







def render_booking_date_analysis():
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Ensure the 'Booking_Date' column is of datetime type
    df['Booking_Date'] = pd.to_datetime(df['Booking_Date'])

    # Extract month and year from the booking date
    df['Booking_Month'] = df['Booking_Date'].dt.strftime('%b %Y')

    # Count the number of bookings per month
    booking_counts = df['Booking_Month'].value_counts().reset_index()
    booking_counts.columns = ['Month', 'Bookings']

    # Sort the data by month
    booking_counts = booking_counts.sort_values(by='Month')

    # Create a bar chart with colors representing different months
    fig = px.bar(booking_counts, x='Month', y='Bookings',
                 title='Booking Patterns Over Time',
                 labels={'Month': 'Month and Year', 'Bookings': 'Number of Bookings'},
                 color='Month')

    # Customize the layout (optional)
    fig.update_xaxes(categoryorder='total ascending')
    fig.update_layout(xaxis_title="Month and Year", yaxis_title="Number of Bookings")

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html




def total_revenue_chart():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Create a line chart for total revenue over time
    total_revenue_chart = px.line(df, x='Booking_Date', y='Total_Revenue_usd',
                                   title='Total Revenue Over Time',
                                   labels={'Booking_Date': 'Booking Date', 'Total_Revenue_usd': 'Total Revenue (USD)'})

    # Customize the layout (optional)
    total_revenue_chart.update_traces(line=dict(color='blue'))  # Change line color



    # Convert the charts to HTML
    chart_html = total_revenue_chart.to_html(full_html=False, include_plotlyjs='cdn')
    

    return chart_html

def render_revenue_analysis_charts():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    

    # Create a line chart for RevPAR over time
    revpar_chart = px.line(df, x='Booking_Date', y='RevPAR_usd',
                            title='RevPAR Over Time',
                            labels={'Booking_Date': 'Booking Date', 'RevPAR_usd': 'RevPAR (USD)'})

    # Customize the layout (optional)
    revpar_chart.update_traces(line=dict(color='green'))  # Change line color

    # Convert the charts to HTML
    
    chart_html = revpar_chart.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html



def render_amenities_preference_chart():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

    # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Group the data by amenities and count the number of guests preferring each amenity
    amenities_preference = df['Amenities'].value_counts()

    # Create a bar chart using Plotly Express
    fig = px.bar(amenities_preference, x=amenities_preference.index, y=amenities_preference.values,
                 title='Amenities Preference Among Guests',
                 labels={'x': 'Amenities', 'y': 'Number of Guests'}, color=amenities_preference.index)

    # Customize the layout (optional)
    fig.update_xaxes(categoryorder='total descending')
    fig.update_layout(showlegend=False)

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html




def render_age_distribution_chart():
    # Load your dataset (adjust the path)
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'HOTELDATA.csv')

   # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')

    # Create a histogram using Plotly Express
    fig = px.histogram(df, x='Age', title='Age Distribution of Guests')

    # Customize the layout (optional)
    fig.update_layout(
        xaxis_title='Age',
        yaxis_title='Count',
        bargap=0.1,
    )

    # Convert the chart to HTML
    chart_html1 = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html1



# Function to find the highest-paid guest
def highest_paid_guest():
    sorted_df = df.sort_values(by='Rate_Paid', ascending=False)
    highest_paid_guest = sorted_df.iloc[0]['Guest_Name']
    return highest_paid_guest

# Function to find the room type of the highest-paid guest
def room_type_of_highest_paid_guest():
    sorted_df = df.sort_values(by='Rate_Paid', ascending=False)
    room_type = sorted_df.iloc[0]['Room_Type']
    return room_type

# Function to find the email address of the highest-paid guest
def email_of_highest_paid_guest():
    sorted_df = df.sort_values(by='Rate_Paid', ascending=False)
    email = sorted_df.iloc[0]['Email_Address']
    return email

# Function to query ChatGPT based on user input
def chat(request):
    response_sentence = ""
    interactions = request.session.get('interactions', [])

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip().lower()

        # Check if the user input mentions a specific guest name
        guest_name = None
        doc = nlp(user_input)
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                guest_name = ent.text
                break

        if guest_name:
            # Extract information for the specified guest
            guest_info = extract_guest_info(guest_name)
            if guest_info:
                response_sentence = f"Here is some information for {guest_name}:\n\n"
                response_sentence += guest_info
            else:
                response_sentence = f"Sorry, I couldn't find information for {guest_name}."
        else:
            # Handle other user queries
            synonyms = {
    'highest paid guest': ['highest paid guest', 'top-paying guest', 'most expensive guest', 'priciest guest', 'premier-paying guest', 'most lavish guest', 'luxury spender', 'elite guest', 'top-dollar guest', 'VVIP spender', 'ultimate payer', 'top-tier guest', 'extravagant guest'],
    'room type of highest paid guest': ['room type of highest paid guest', 'accommodation type of highest paid guest', 'suite type of top-paying guest', 'lodging category of most expensive guest', 'premium room type for priciest guest', 'luxury suite chosen by premier-paying guest', 'accommodation selection for the most lavish guest', 'room type preferred by the elite guest', 'top-dollar guests lodging choice', 'VVIP spenders suite type', 'ultimate payers accommodation type', 'room category for top-tier guest', 'accommodation class for extravagant guest'],
    'email of highest paid guest': ['email of highest paid guest', 'email address of top-paying guest', 'email for most expensive guest', 'priciest guests email', 'email contact for premier-paying guest', 'most lavish guests email', 'luxury spenders email', 'elite guests email', 'top-dollar guests email address', 'VVIP spenders email', 'ultimate payers email', 'top-tier guests email', 'extravagant guests email'],
    'promotion image': ['promotion image', 'promotion sample', 'promotion', 'promotional image', 'promo picture', 'promo', 'advertising image', 'marketing visual', 'campaign graphic', 'advertisement picture', 'promo photo', 'marketing image', 'marketing sample', 'ad image', 'commercial visual', 'promotional artwork', 'campaign photo'],
    'thanks image': ['thanks image', 'thanks card', 'thank you image', 'thank you card', 'gratitude card', 'appreciation image', 'appreciation card', 'thankful card', 'acknowledgment image', 'guest appreciation card', 'hotel thank you image', 'hotel thank you card', 'customer gratitude image', 'customer gratitude card', 'hospitality thank you card', 'guest thanksgiving image', 'guest thanksgiving card', 'client appreciation card', 'service thank you image', 'guest recognition image', 'hospitality appreciation card', 'guest acknowledgment image', 'hospitality gratitude image', 'hospitality gratitude card', 'client thank you card', 'customer thanks image', 'customer thanks card', 'acknowledgment card'],
    'welcome image': ['welcome image', 'welcome card', 'greeting picture', 'greeting card', 'reception image', 'arrival visual', 'warmth photo', 'hospitality welcome image', 'guest reception picture', 'guest reception card', 'hospitality greeting image', 'arrival photo', 'arrival card', 'guest welcome picture', 'hospitality arrival image', 'hospitality arrival card', 'hospitality reception visual', 'guest arrival image', 'warm welcome photo', 'warm welcome card', 'hospitality greeting visual', 'hospitality arrival picture', 'guest reception photo', 'cordial welcome image', 'cordial welcome card', 'guest arrival visual', 'guest arrival card', 'friendly greeting picture'],
    'showppt': ['give me a dashboard sample', 'provide a report example', 'report example', 'report', 'presentation', 'show a presentation sample', 'display a reporting template', 'reporting', 'demonstrate a dashboard', 'dashboard', 'exhibit a sample presentation', 'present a report prototype', 'reveal a presentation model',  'share a reporting example', 'show a report illustration', 'distribute a presentation demo', 'offer a reporting mockup', 'unveil a dashboard showcase', 'expose a report representation', 'illustrate a presentation specimen', 'uncover a reporting instance', 'display a dashboard model', 'present a sample report', 'demonstrate a presentation draft', 'show a report outline'],
    'visualisation of data travelers': ['visualization of data travelers', 'data traveler visualization', 'data traveler visualization techniques', 'visualization for data explorers', 'data traveler visualization methods', 'data traveler visual analysis', 'visual data traveler insights', 'data traveler data visualization', 'data traveler visual representation', 'data explorer visualization'],
    'Gender Distribution of Guests': ['gender distribution of guests', 'guest gender distribution', 'guest gender demographics', 'gender composition of guests', 'guests by gender', 'guests gender', 'gender of guests', 'gender guests', 'guest gender analysis', 'gender guest analysis', 'gender analysis', 'guest gender percentage', 'gender diversity of guests', 'guest gender breakdown', 'gender guest breakdown', 'guest gender statistics', 'gender guest statistics', 'guest gender profiling'],
    'Age Distribution of Guests': ['age distribution of guests', 'guest age distribution', 'age distribution', 'guest age demographics', 'age composition of guests', 'guests by age', 'guest age analysis', 'age analysis', 'age diversity of guests', 'guest age breakdown', 'age breakdown', 'guest age statistics', 'age statistics', 'age profiling', 'guest age profiling'],
    'Travel Purpose Analysis': ['travel purpose analysis', 'purpose of travel analysis', 'purpose analysis', 'travel motivation analysis', 'analysis of travel intent', 'travel purpose study', 'reasons for travel analysis', 'reasons for travel', 'reasons of travel', 'travel objective analysis', 'travel purpose examination', 'travel intent analysis', 'purpose-driven travel analysis'],
    'Loyalty Membership Analysis': ['loyalty membership analysis', 'loyalty program analysis', 'membership loyalty analysis', 'loyalty scheme analysis', 'loyalty benefits analysis', 'loyalty rewards analysis', 'loyalty card analysis', 'loyalty program membership analysis', 'loyalty analysis for members', 'loyalty scheme membership analysis'],
    'Booking Patterns Over Time': ['booking patterns over time', 'reservation trends over time', 'booking behavior analysis', 'historical booking analysis', 'booking trends analysis', 'booking habits over time', 'reservation pattern analysis', 'booking history analysis', 'booking trends over time', 'reservation booking analysis'],
    'Length of Stay Analysis': ['length of stay analysis', 'stay duration analysis', 'guest visit duration analysis', 'duration of guest stays', 'stay length trends analysis', 'guest accommodation duration analysis', 'guest visit length analysis', 'guest stay duration examination', 'length of stay pattern analysis', 'stay duration trend analysis'],
    'Source of Booking Analysis': ['source of booking analysis', 'booking channel analysis', 'reservation source analysis', 'booking origin analysis', 'booking platform analysis', 'booking source trends', 'booking channel distribution analysis', 'booking source breakdown', 'reservation channel analysis', 'booking channel trends'],
    'Total Revenue Over Time': ['total revenue over time', 'revenue trends analysis', 'historical revenue analysis', 'revenue accumulation analysis', 'revenue growth over time', 'revenue generation trends', 'total income analysis', 'revenue over time examination', 'income trends analysis', 'revenue accumulation over time'],
    'RevPAR Over Time': ['revpar over time', 'revenue per available room analysis', 'revpar trends analysis', 'revpar growth over time', 'room revenue analysis', 'revpar performance over time', 'revpar trends examination', 'revpar variation analysis', 'average room revenue trends', 'room revenue per available room analysis'],
    'Amenities Preference Among Guests': ['amenities preference among guests', 'guest amenities choice', 'guest amenity preferences', 'amenity selection by guests', 'guests amenities favor', 'preferred guest amenities', 'guest amenity choice analysis', 'amenities of choice among guests', 'amenity preference analysis', 'guests amenity favoritism'],
    'Trends Over Time': ['trends over time', 'time-based trends analysis', 'historical trend analysis', 'trend evolution analysis', 'long-term trend assessment', 'time-span trends analysis', 'trends development over time', 'trend pattern analysis', 'trend variation over time', 'trends and time analysis'],
    'Average Occupancy Rate Over Time': ['average occupancy rate over time', 'occupancy trends analysis', 'historical occupancy rate analysis', 'occupancy rate over time', 'occupancy performance analysis', 'occupancy rate trends analysis', 'occupancy duration over time', 'occupancy rate variation analysis', 'average room occupancy analysis', 'room occupancy trends over time'],
    'GOP PAR vs. Month': ['gop par vs. month', 'gop par monthly comparison', 'gop par by month analysis', 'gop par month-to-month analysis', 'gop par vs. time', 'gop par performance over months', 'gop par variation by month', 'gop par monthwise analysis', 'gop par comparison over time', 'gop par monthly trend analysis'],
    'Revenue Generation Index Analysis': ['revenue generation index analysis', 'income generation index analysis', 'revenue productivity analysis', 'revenue efficiency analysis', 'income generation assessment', 'revenue index performance analysis', 'revenue generation trend analysis', 'income productivity examination', 'revenue index analysis', 'revenue generation assessment'],
    'MCPB Analysis Over Time': ['mcpb analysis over time', 'mcpb trends analysis', 'historical mcpb analysis', 'mcpb performance over time', 'mcpb growth analysis', 'mcpb variation over time', 'mcpb trends examination', 'mcpb trends over time', 'mcpb analysis by time', 'mcpb assessment over time'],
    'Sentiment Score Analysis': ['sentiment score analysis', 'guest sentiment analysis', 'guest review sentiment analysis', 'sentiment analysis of guest feedback', 'guest sentiment score examination', 'sentiment trend analysis', 'guest sentiment rating analysis', 'sentiment analysis of reviews', 'guest sentiment assessment', 'sentiment score trends analysis'],
    'Room Type Distribution': ['room type distribution', 'guest room type distribution', 'room category distribution', 'room type allocation', 'room type diversity', 'room type variety', 'distribution of guest room types', 'room category breakdown', 'guest room type variety', 'room type distribution analysis']
}


            # Check user input against synonyms
            matched_intent = None
            for intent, variations in synonyms.items():
                if any(variation in user_input for variation in variations):
                    matched_intent = intent
                    break  # Exit the loop when a match is found

            if matched_intent:
                # Handle matched intent
                if matched_intent == 'highest paid guest':
                    response_sentence = f"The highest-paid guest is: {highest_paid_guest()}"
                elif matched_intent == 'room type of highest paid guest':
                    response_sentence = f"The room type of the highest-paid guest is: {room_type_of_highest_paid_guest()}"
                elif matched_intent == 'email of highest paid guest':
                    response_sentence = f"The email address of the highest-paid guest is: {email_of_highest_paid_guest()}"
                elif matched_intent == 'promotion image':
                    html_image1 = showimages1(request)
                    response_sentence = f"The promotion image is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'html_image1': html_image1,
                        'interactions': interactions,
                    })
                elif matched_intent == 'thanks image':
                    html_image2 = showimages2(request)
                    response_sentence = f"The thank you image is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'html_image2': html_image2,
                        'interactions': interactions,
                    })
                elif matched_intent == 'welcome image':
                    html_image3 = showimages3(request)
                    response_sentence = f"The welcome image is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'html_image3': html_image3,
                        'interactions': interactions,
                    })
                elif matched_intent == 'showppt':
                    ppt_files = showppt(request)
                    response_sentence = f"The presentation is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'ppt': ppt_files,
                        'interactions': interactions,
                    })
                elif matched_intent == 'visualisation of data travelers':
                    chart_html = render_selected_plots()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Gender Distribution of Guests':
                    chart_html1 = render_gender_distribution_chart()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html1': chart_html1,
                        'interactions': interactions,
                    })
                
                elif matched_intent == 'Age Distribution of Guests':
                    chart_html1 = render_age_distribution_chart()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html1': chart_html1,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Travel Purpose Analysis':
                    chart_html = render_travel_purpose_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Loyalty Membership Analysis':
                    chart_html = render_loyalty_membership_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Booking Patterns Over Time':
                    chart_html = render_booking_date_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Length of Stay Analysis':
                    chart_html = stay_charts()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Room Type Distribution':
                    chart_html = render_room_type_distribution_chart()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Source of Booking Analysis':
                    chart_html = render_source_of_booking_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                
                elif matched_intent == 'Total Revenue Over Time':
                    chart_html = total_revenue_chart()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                
                elif matched_intent == 'RevPAR Over Time':
                    chart_html = render_revenue_analysis_charts()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Amenities Preference Among Guests':
                    chart_html = render_amenities_preference_chart()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                
                elif matched_intent == 'Trends Over Time':
                    chart_html = visualize_trends_over_time()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Average Occupancy Rate Over Time':
                    chart_html = analyze_occupancy_rate()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'GOP PAR vs. Month':
                    chart_html = plot_gop_par_vs_month()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Revenue Generation Index Analysis':
                    chart_html = revenue_generation_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                
                elif matched_intent == 'MCPB Analysis Over Time':
                    chart_html = mcpb_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                elif matched_intent == 'Sentiment Score Analysis':
                    chart_html = sentiment_score_analysis()
                    response_sentence = f"The chart is displayed below:"
                    return render(request, 'chat.html', {
                        'response_sentence': response_sentence,
                        'chart_html': chart_html,
                        'interactions': interactions,
                    })
                

            else:
                # Call OpenAI GPT-3 API for other user input
                response_sentence = generate_response(user_input)


            

        interactions.append((user_input, response_sentence))
        request.session['interactions'] = interactions

    elif request.method == 'GET' and 'clear_history' in request.GET:
        # Clear the interaction history by resetting the session data
        request.session['interactions'] = []
        # Redirect back to the same page after clearing history
        return redirect('chat')

    return render(request, 'chat.html', {
        'response_sentence': response_sentence,
        'interactions': interactions,
    })

# Function to extract guest information based on the specified name
def extract_guest_info(guest_name):
    # Search the DataFrame for guest information
    guest_data = df[df['Guest_Name'].str.lower() == guest_name.lower()]

    if not guest_data.empty:
        
        
        info = f"Guest Name: {guest_data['Guest_Name'].values[0]}\n"
        info += f"Age: {guest_data['Age'].values[0]}\n"
        info += f"Location: {guest_data['Location'].values[0]}\n"
        info += f"Travel Purpose: {guest_data['Travel_Purpose'].values[0]}\n"
        info += f"Loyalty Membership: {guest_data['Loyalty_Membership'].values[0]}\n"
        info += f"Booking Date: {guest_data['Booking_Date'].values[0]}\n"
        info += f"Length of Stay: {guest_data['Length_of_Stay'].values[0]} nights\n"
        info += f"Booking Channel: {guest_data['Booking_Channel'].values[0]}\n"
        info += f"Amenities: {guest_data['Amenities'].values[0]}\n"
        info += f"Email Address: {guest_data['Email_Address'].values[0]}\n"

        return info

    return None

# Function to generate a response using OpenAI GPT-3
def generate_response(user_input):
    try:
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.5,
        max_tokens=100
    )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"




def visualize_trends_over_time():
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    data = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create an interactive line chart
    fig = px.line(data, x='Month', y=['Total Available Rooms', 'Average Daily Rate', 'RevPar'],
                  title='Trends Over Time',
                  labels={'Month': 'Month', 'value': 'Value'},
                  color_discrete_map={'Total Available Rooms': 'blue', 'Average Daily Rate': 'green', 'RevPar': 'red'})

    # Customize the layout (optional)
    fig.update_traces(marker=dict(size=8))

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html


def analyze_occupancy_rate():

    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    df = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create a copy of the DataFrame and convert the "Average Occupancy Rate" column to numeric

    df['Average Occupancy Rate'] = df['Average Occupancy Rate'].str.rstrip('%').astype(float)

    # Create a line chart to visualize the "Average Occupancy Rate" over time
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['Month'], y=df['Average Occupancy Rate'], mode='lines+markers',
                             name='Occupancy Rate', line=dict(color='blue')))

    # Customize the layout
    fig.update_layout(title='Average Occupancy Rate Over Time',
                      xaxis_title='Month',
                      yaxis_title='Occupancy Rate (%)',
                      hovermode='x unified')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html


def plot_gop_par_vs_month():

    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    data = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create a line chart to compare GOP PAR across months
    fig = px.line(data, x='Month', y='GOP PAR', title='GOP PAR vs. Month',
                  labels={'Month': 'Month', 'GOP PAR': 'GOP PAR'})

    # Customize the layout (optional)
    fig.update_traces(marker=dict(size=10), line=dict(width=2), mode='lines+markers')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html



def revenue_generation_analysis():
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    data = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create a bar chart to visualize the Revenue Generation Index (RGI) over months
    fig = px.bar(data, x='Month', y='Revenue Generation Index', color='Revenue Generation Index',
                 title='Revenue Generation Index Analysis',
                 labels={'Month': 'Month', 'Revenue Generation Index': 'RGI'},
                 color_continuous_scale='Viridis')

    # Customize the layout (optional)
    fig.update_xaxes(type='category')  # Ensure months are displayed in order
    fig.update_coloraxes(colorbar_title='RGI Color Scale')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html




def mcpb_analysis():

    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    data = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create an interactive line chart for MCPB over time
    fig = px.line(data, x='Month', y='MCPB', title='MCPB Analysis Over Time',
                  labels={'Month': 'Month', 'MCPB': 'Marketing Cost Per Booking'},
                  color_discrete_sequence=['blue'])

    # Customize the layout (optional)
    fig.update_traces(marker=dict(size=8))
    fig.update_xaxes(type='category')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html



def sentiment_score_analysis():
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'KPIs.csv')

   # Read the CSV file into a DataFrame for hotels
    data = pd.read_csv(csv_file_path, encoding='iso-8859-2')
    # Create an interactive line chart to visualize the Sentiment Score over months
    fig = px.line(data, x='Month', y='Sentiment Score on TripAdvisor',
                  title='Sentiment Score Analysis on TripAdvisor',
                  labels={'Month': 'Month', 'Sentiment Score on TripAdvisor': 'Sentiment Score'},
                  markers=True, color_discrete_sequence=px.colors.qualitative.Set1)

    # Customize the layout (optional)
    fig.update_traces(mode='lines+markers')

    # Convert the chart to HTML
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return chart_html
