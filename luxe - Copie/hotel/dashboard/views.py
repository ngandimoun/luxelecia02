from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import os

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import os

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import os
import uuid  # Import the uuid module for generating unique IDs

import uuid

# ...

def create_dashboard_item(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        summary = request.POST.get('summary', '')
        images = request.FILES.getlist('images')

        # Generate a unique UUID as the item_id
        item_id = uuid.uuid4()

        # Initialize empty lists for image URLs and item data
        image_urls = []
        item_data = {'id': item_id, 'title': title, 'summary': summary, 'image_urls': image_urls}

        # Handle multiple image uploads
        for image in images:
            if image:
                fs = FileSystemStorage()
                image_filename = fs.save(image.name, image)
                image_url = fs.url(image_filename)
                image_urls.append(image_url)

        # Check if there's any data provided (title, summary, or images)
        if title or summary or image_urls:
            # Store the item data in the session or a list, depending on your needs
            if 'dashboard_items' not in request.session:
                request.session['dashboard_items'] = []
            request.session['dashboard_items'].append(item_data)

            # Redirect to the dashboard page after adding the item
            return redirect('dashboard:dashboard')

    return render(request, 'create_dashboard_item.html')



def dashboard(request):
    dashboard_items = request.session.get('dashboard_items', [])
    return render(request, 'dashboard.html', {'dashboard_items': dashboard_items})




def download_dashboard(request, item_id):
    # Retrieve the dashboard item data (you should adapt this part to your session data structure)
    dashboard_items = request.session.get('dashboard_items', [])

    # Find the dashboard item with the specified item_id
    for item in dashboard_items:
        if item.get('id') == item_id:
            # Get the file path (you should adapt this part to your data structure)
            file_path = item.get('file_path', '')

            # Ensure the file path is not empty
            if file_path:
                # Construct the file response
                file_name = os.path.basename(file_path)
                with open(file_path, 'rb') as f:
                    response = HttpResponse(File(f), content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response

    # Handle the case when the item_id is not found or file_path is empty
    return HttpResponse("File not found", status=404)
