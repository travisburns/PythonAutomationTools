from googlesearch import search

def search_nearby_businesses(query):
    search_query = f"{query} nearby businesses"

    businesses = []

    # Perform Google search
    search_results = search(search_query, num_results=5)

    # Extract business information
    for result in search_results:
        businesses.append({
            'name': result,
            'website': None  # We'll extract the website separately
        })

    return businesses

def extract_website(url):
    # This function should be improved to extract the actual website URL from the search result
    return url

def main():
    search_term = input("Enter a search term for nearby businesses: ")
    businesses = search_nearby_businesses(search_term)

    if businesses:
        for idx, business in enumerate(businesses, start=1):
            website = extract_website(business['name'])
            business['website'] = website

            print(f"\nBusiness {idx}:\nName: {business['name']}\nWebsite: {business['website']}")
    else:
        print("No businesses found.")

if __name__ == "__main__":
    main()