def test_scrape(py):
    URL='https://www.pharmacyappointments.ca/'
    py.visit(URL)    
    py.contains('Continue').click()
    py.get('#q-screening-province').select('Ontario')

