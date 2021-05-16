import time
def _log(prop):
    with open('log', 'a') as f:
        print(prop, file=f)

def _get_sched():
    pass

def _num_avail_locs(py):
    """Number of available locations"""
    btns=py.find('[type="button"]') 
    return len(btns)

def test_scrape(py):
    URL='https://www.pharmacyappointments.ca/'
    py.visit(URL)    
    py.contains('Continue').click()
    py.get('#q-screening-province').select('Ontario')
    py.contains('Yes').click()
    py.contains('Continue').click()
    py.get('#location-search-input').type('M5S')
    py.contains('Continue').click()
    py.contains('Continue').click()
    btn_txt='See all availability'
    py.contains(btn_txt).click()
    #TODO iterate through each available booking
    n = _num_avail_locs(py)