#!/usr/bin/env python
import requests
from variables import *


def search(search_parameter):
    # Prepare search payload
    parameters = {'keywords': search_parameter, 'max': max, 'state': state, 'sortBy': sort_by,
                  'costToCompleteRange': cost_to_complete_range, 'APIKey': api_token}

    # Make GET call to API and store JSON response
    info = requests.get(url, params=parameters)
    proposals = info.json()
    number_proposals_returned = len(proposals['proposals'])

    # Assert proposals returned is less than equal to the max argument
    assert number_proposals_returned <= max

    # Create empty lists to use for summation of values
    percent_funded = []
    number_of_donors = []
    cost_to_complete = []
    number_of_students = []
    total_price = []

    # Process charities returned
    if number_proposals_returned > 0:
        for charity in proposals['proposals']:
            print '***CHARITY FOR YOUR CONSIDERATION***'
            assert charity['stateFullName'] == state_fullname
            assert float(charity['costToComplete']) >= min_funding_cost
            assert float(charity['costToComplete']) <= max_funding_cost
            print 'Title: ' + charity['title']
            print 'Short Description: ' + charity['shortDescription']
            print 'ProposalURL: ' + charity['proposalURL']
            print 'Cost To Complete: ' + charity['costToComplete']
            percent_funded.append(float(charity['percentFunded']))
            number_of_donors.append(int(charity['numDonors']))
            number_of_students.append(int(charity['numStudents']))
            cost_to_complete.append(float(charity['costToComplete']))
            total_price.append(float(charity['totalPrice']))

        # Calculate averages for all charitites returned
        print '***AVERAGES FOR ALL CHARITIES***'
        print 'Average Percent Funded: ', sum(percent_funded)/number_proposals_returned
        print 'Average Number of Donors: ', sum(number_of_donors)/number_proposals_returned
        print 'Average Number of Students: ', sum(number_of_students)/number_proposals_returned
        print 'Average Cost to Complete: ', sum(cost_to_complete)/number_proposals_returned
        print 'Average Total Price: ', sum(total_price)/number_proposals_returned

    # Print error message if no charity was returned for search term
    else:
        print 'No charities returned for search term ' + search_parameter

