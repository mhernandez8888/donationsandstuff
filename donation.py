#!/usr/bin/env python
import DonationLib


if __name__ == '__main__':
    search_parameter = raw_input("Search Term = ")
    DonationLib.search(search_parameter)