def html_to_json(html_str):
    items = [item.strip() for item in html_str.split('</li><li>')]
    return {
        'address':{
            'state':items[2],
            'district':items[3],
            'block':items[4],
            'cluster':items[5],
            'village':items[7],
            'pincode':items[8],
        },
        'school_profile':{
            'school_name':items[0].replace('<ul><li>',''),
            'udise_code':items[1],
            'school_category':items[9],
            'school_type':items[10],
            'class_from':int(items[11]),
            'class_to':int(items[12]),
            'state_management':items[13],
            'national_management':items[14],
            'status':items[15],
            'location':items[16],
        },
        'basic_details': {
            'aff_board_sec':items[34],
            'aff_board_hsec':items[35],
            'year_of_establishment':int(items[36]),
            'pre_primary':items[37],
        },
        'facilities': {
            'building_status':items[38],
            'boundary_wall':items[39],
            'no_of_boys_toilets':int(items[40]),
            'no_of_girls_toilets':int(items[41]),
            'no_of_cwsn_toilets':int(items[42]),
            'drinking_water_availability':True if items[43]=='Yes' else False, # yes
            'hand_wash_facility':True if items[43]=='Yes' else False, # yes
            'functional_generator':int(items[45]),
            'library':True if items[46]=='1-Yes' else False, # yes items[46],
            'reading_corner':True if items[47]=='1-Yes' else False, # items[47],
            'book_bank':True if items[49]=='1-Yes' else False, # items[49],
            'functional_laptop':int(items[51]),
            'functional_desktop':int(items[52]),
            'functional_tablet':int(items[53]),
            'functional_scanner':int(items[54]),
            'functional_printer':int(items[55]),
            'functional_led':int(items[56]),
            'functional_digiboard':int(items[57]),
            'internet':True if items[58]=='1-Yes' else False, # items[58],
            'dth':True if items[59]=='1-Yes' else False, # items[59],
            'functional_web_cam':int(items[60]),
        },
        'room_details':{
            'class_rooms':int(items[61]),
            'other_rooms':int(items[62]),
        },
        'enrolment_of_the_students':[items[63],items[64],items[65],items[66],items[67],items[68],items[69],items[70],items[71],items[72],items[73],items[74],items[75],],  # ['37','12','37','12','37','12','37','12','37','12','37','12','last'],
        'total_teachers':int(items[76].split()[2]),
    }