
from mongoMethods import getAllMongo
from openAIModule import aiProcess
import random

#coicop codes---------------------------------------------------
def findCoicop(company_name, all_data):
  #define a lsit of all of the high level catagories of coicop codes.
  coicop_categories = [
    {"Code": "01", "Description": "Food and non-alcoholic beverages"},
    {"Code": "02", "Description": "Alcoholic beverages, tobacco and narcotics"},
    {"Code": "03", "Description": "Clothing and footwear"},
    {"Code": "04", "Description": "Housing, water, electricity, gas and other fuels"},
    {"Code": "05", "Description": "Furnishings, household equipment and routine household maintenance"},
    {"Code": "06", "Description": "Health"},
    {"Code": "07", "Description": "Transport"},
    {"Code": "08", "Description": "Information and communication"},
    {"Code": "09", "Description": "Recreation, sport and culture"},
    {"Code": "10", "Description": "Education services"},
    {"Code": "11", "Description": "Restaurants and accommodation services"},
    {"Code": "12", "Description": "Insurance and financial services"},
    {"Code": "13", "Description": "Personal care, social protection and miscellaneous goods and services"},
    {"Code": "14", "Description": "Individual consumption expenditure of non-profit institutions serving households (NPISHS)"},
    {"Code": "15", "Description": "Individual consumption expenditure of general government"}
]

  promptHighLevelCatagories="Please read the following catagories of coicop codes and the information about a company"+all_data+", then determine which catagory their product falls under(respond with only the number of the catagory for example '04'):"
  for item in coicop_categories:
     strItem=str(item)
     promptHighLevelCatagories+="/n"+strItem

  hLSection=aiProcess(promptHighLevelCatagories)
  

  #lists for each section
  section_1 = [
    {"Code": "01", "Description": "FOOD AND NON-ALCOHOLIC BEVERAGES",
     "Subcategories": [
        {"Code": "01.1", "Description": "FOOD",
         "Subcategories": [
            {"Code": "01.1.1", "Description": "Cereals and cereal products (ND)",
             "Subcategories": [
                {"Code": "01.1.1.1", "Description": "Cereals (ND)"},
                {"Code": "01.1.1.2", "Description": "Flour of cereals (ND)"},
                {"Code": "01.1.1.3", "Description": "Bread and bakery products (ND)"},
                {"Code": "01.1.1.4", "Description": "Breakfast cereals (ND)"},
                {"Code": "01.1.1.5", "Description": "Macaroni, noodles, couscous and similar pasta products (ND)"},
                {"Code": "01.1.1.9", "Description": "Other cereal and grain mill products (ND)"}
            ]},
            {"Code": "01.1.2", "Description": "Live animals, meat and other parts of slaughtered land animals (ND)",
             "Subcategories": [
                {"Code": "01.1.2.1", "Description": "Live land animals (ND)"},
                {"Code": "01.1.2.2", "Description": "Meat, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.2.3", "Description": "Meat, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.2.4", "Description": "Offal, blood and other parts of slaughtered animals, fresh, chilled or frozen, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.2.5", "Description": "Meat, offal, blood and other parts of slaughtered animals' preparations (ND)"}
            ]},
            {"Code": "01.1.3", "Description": "Fish and other seafood (ND)",
             "Subcategories": [
                {"Code": "01.1.3.1", "Description": "Fish, live, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.3.2", "Description": "Fish, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.3.3", "Description": "Fish preparations (ND)"},
                {"Code": "01.1.3.4", "Description": "Other seafood, live, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.3.5", "Description": "Other seafood, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.3.6", "Description": "Other seafood preparations (ND)"},
                {"Code": "01.1.3.7", "Description": "Livers, roes and offal of fish and of other seafood in all forms (ND)"}
            ]},
            {"Code": "01.1.4", "Description": "Milk, other dairy products and eggs (ND)",
             "Subcategories": [
                {"Code": "01.1.4.1", "Description": "Raw and whole milk (ND)"},
                {"Code": "01.1.4.2", "Description": "Skimmed milk (ND)"},
                {"Code": "01.1.4.3", "Description": "Other milk and cream (ND)"},
                {"Code": "01.1.4.4", "Description": "Non-animal milk (ND)"},
                {"Code": "01.1.4.5", "Description": "Cheese (ND)"},
                {"Code": "01.1.4.6", "Description": "Yoghurt and similar products (ND)"},
                {"Code": "01.1.4.7", "Description": "Milk-based dessert and beverages (ND)"},
                {"Code": "01.1.4.8", "Description": "Eggs (ND)"},
                {"Code": "01.1.4.9", "Description": "Other dairy products (ND)"}
            ]},
            {"Code": "01.1.5", "Description": "Oils and fats (ND)",
             "Subcategories": [
                {"Code": "01.1.5.1", "Description": "Vegetable oils (ND)"},
                {"Code": "01.1.5.2", "Description": "Butter and other fats and oils derived from milk (ND)"},
                {"Code": "01.1.5.3", "Description": "Margarine and similar preparations (ND)"},
                {"Code": "01.1.5.9", "Description": "Other animal oils and fats (ND)"}
            ]},
            {"Code": "01.1.6", "Description": "Fruits and nuts (ND)",
             "Subcategories": [
                {"Code": "01.1.6.1", "Description": "Dates, figs and tropical fruits, fresh (ND)"},
                {"Code": "01.1.6.2", "Description": "Citrus fruits, fresh (ND)"},
                {"Code": "01.1.6.3", "Description": "Stone fruits and pome fruits, fresh (ND)"},
                {"Code": "01.1.6.4", "Description": "Berries, fresh (ND)"},
                {"Code": "01.1.6.5", "Description": "Other fruits, fresh (ND)"},
                {"Code": "01.1.6.6", "Description": "Frozen fruit (ND)"},
                {"Code": "01.1.6.7", "Description": "Fruit, dried and dehydrated (ND)"},
                {"Code": "01.1.6.8", "Description": "Nuts, in shell or shelled (ND)"},
                {"Code": "01.1.6.9", "Description": "Fruit and nuts ground and other preparations (ND)"}
            ]},
            {"Code": "01.1.7", "Description": "Vegetables, tubers, plantains, cooking bananas and pulses (ND)",
             "Subcategories": [
                {"Code": "01.1.7.1", "Description": "Leafy or stem vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.2", "Description": "Fruit-bearing vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.3", "Description": "Green leguminous vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.4", "Description": "Other vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.5", "Description": "Tubers, plantains and cooking bananas (ND)"},
                {"Code": "01.1.7.6", "Description": "Pulses (ND)"},
                {"Code": "01.1.7.7", "Description": "Other vegetables, tubers, plantains and cooking bananas, dried and dehydrated (ND)"},
                {"Code": "01.1.7.8", "Description": "Vegetables, tubers, plantains and cooking bananas, frozen (ND)"},
                {"Code": "01.1.7.9", "Description": "Vegetables, tubers, plantains, cooking bananas and pulses ground and other preparations (ND)"}
            ]},
            {"Code": "01.1.8", "Description": "Sugar, confectionery and desserts (ND)",
             "Subcategories": [
                {"Code": "01.1.8.1", "Description": "Cane and beet sugar (ND)"},
                {"Code": "01.1.8.2", "Description": "Other sugar and sugar substitutes (ND)"},
                {"Code": "01.1.8.3", "Description": "Jams, fruit jellies, marmalades, fruit purée and pastes, honey (ND)"},
                {"Code": "01.1.8.4", "Description": "Nut purée, nut butter and nut pastes (ND)"},
                {"Code": "01.1.8.5", "Description": "Chocolate, cocoa, and cocoa-based food products (ND)"},
                {"Code": "01.1.8.6", "Description": "Ice, ice cream and sorbet (ND)"},
                {"Code": "01.1.8.9", "Description": "Other sugar confectionery and desserts n.e.c. (ND)"}
            ]},
            {"Code": "01.1.9", "Description": "Ready-made food and other food products n.e.c. (ND)",
             "Subcategories": [
                {"Code": "01.1.9.1", "Description": "Ready-made food (ND)"},
                {"Code": "01.1.9.2", "Description": "Baby food (ND)"},
                {"Code": "01.1.9.3", "Description": "Salt, condiments and sauces (ND)"},
                {"Code": "01.1.9.4", "Description": "Spices, culinary herbs and seeds (ND)"},
                {"Code": "01.1.9.9", "Description": "Other food products n.e.c. (ND)"}
            ]}
         ]},
         {"Code": "01.2", "Description": "NON-ALCOHOLIC BEVERAGES",
          "Subcategories": [
            {"Code": "01.2.1", "Description": "Fruit and vegetable juices (ND)",
             "Subcategories": [
                {"Code": "01.2.1.0", "Description": "Fruit and vegetable juices (ND)"}
             ]},
            {"Code": "01.2.2", "Description": "Coffee and coffee substitutes (ND)",
             "Subcategories": [
                {"Code": "01.2.2.0", "Description": "Coffee and coffee substitutes (ND)"}
             ]},
            {"Code": "01.2.3", "Description": "Tea, maté and other plant products for infusion (ND)",
             "Subcategories": [
                {"Code": "01.2.3.0", "Description": "Tea, maté and other plant products for infusion (ND)"}
             ]},
            {"Code": "01.2.4", "Description": "Cocoa drinks (ND)",
             "Subcategories": [
                {"Code": "01.2.4.0", "Description": "Cocoa drinks (ND)"}
             ]},
            {"Code": "01.2.5", "Description": "Water (ND)",
             "Subcategories": [
                {"Code": "01.2.5.0", "Description": "Water (ND)"}
             ]},
            {"Code": "01.2.6", "Description": "Soft drinks (ND)",
             "Subcategories": [
                {"Code": "01.2.6.0", "Description": "Soft drinks (ND)"}
             ]},
            {"Code": "01.2.9", "Description": "Other non-alcoholic beverages (ND)",
             "Subcategories": [
                {"Code": "01.2.9.0", "Description": "Other non-alcoholic beverages (ND)"}
             ]}
          ]},
         {"Code": "01.3", "Description": "SERVICES FOR PROCESSING PRIMARY GOODS FOR FOOD AND NON-ALCOHOLIC BEVERAGES",
          "Subcategories": [
            {"Code": "01.3.0", "Description": "Services for processing primary goods for food and non-alcoholic beverages (S)",
             "Subcategories": [
                {"Code": "01.3.0.0", "Description": "Services for processing primary goods for food and non-alcoholic beverages (S)"}
             ]}
          ]}
     ]}
  ]
  section_2 = [
    {"Code": "02", "Description": "ALCOHOLIC BEVERAGES, TOBACCO AND NARCOTICS",
     "Subcategories": [
        {"Code": "02.1", "Description": "ALCOHOLIC BEVERAGES",
         "Subcategories": [
            {"Code": "02.1.1", "Description": "Spirits and liquors (ND)",
             "Subcategories": [
                {"Code": "02.1.1.0", "Description": "Spirits and liquors (ND)"}
             ]},
            {"Code": "02.1.2", "Description": "Wine (ND)",
             "Subcategories": [
                {"Code": "02.1.2.1", "Description": "Wine from grapes (ND)"},
                {"Code": "02.1.2.2", "Description": "Wine from other sources (ND)"}
             ]},
            {"Code": "02.1.3", "Description": "Beer (ND)",
             "Subcategories": [
                {"Code": "02.1.3.0", "Description": "Beer (ND)"}
             ]},
            {"Code": "02.1.9", "Description": "Other alcoholic beverages (ND)",
             "Subcategories": [
                {"Code": "02.1.9.0", "Description": "Other alcoholic beverages (ND)"}
             ]}
          ]},
        {"Code": "02.2", "Description": "ALCOHOL PRODUCTION SERVICES",
         "Subcategories": [
            {"Code": "02.2.0", "Description": "Alcohol production services (S)",
             "Subcategories": [
                {"Code": "02.2.0.0", "Description": "Alcohol production services (S)"}
             ]}
          ]},
        {"Code": "02.3", "Description": "TOBACCO",
         "Subcategories": [
            {"Code": "02.3.0", "Description": "Tobacco (ND)",
             "Subcategories": [
                {"Code": "02.3.0.1", "Description": "Cigarettes (ND)"},
                {"Code": "02.3.0.2", "Description": "Cigars (ND)"},
                {"Code": "02.3.0.9", "Description": "Other tobacco products (ND)"}
             ]}
          ]},
        {"Code": "02.4", "Description": "NARCOTICS",
         "Subcategories": [
            {"Code": "02.4.0", "Description": "Narcotics (ND)",
             "Subcategories": [
                {"Code": "02.4.0.0", "Description": "Narcotics (ND)"}
             ]}
          ]}
     ]}
]
  section_3 = [
    {"Code": "03", "Description": "Clothing and footwear",
     "Subcategories": [
         {"Code": "03.1", "Description": "Clothing",
          "Subcategories": [
              {"Code": "03.1.1", "Description": "Clothing materials (SD)",
               "Subcategories": [
                   {"Code": "03.1.1.0", "Description": "Clothing materials (SD)"}
               ]},
              {"Code": "03.1.2", "Description": "Garments (SD)",
               "Subcategories": [
                   {"Code": "03.1.2.1", "Description": "Garments for men or boys (SD)"},
                   {"Code": "03.1.2.2", "Description": "Garments for women or girls (SD)"},
                   {"Code": "03.1.2.3", "Description": "Garments for infants (0 to under 2 years) (SD)"},
                   {"Code": "03.1.2.4", "Description": "School uniforms (SD)"}
               ]},
              {"Code": "03.1.3", "Description": "Other articles of clothing and clothing accessories (SD)",
               "Subcategories": [
                   {"Code": "03.1.3.1", "Description": "Other articles of clothing (SD)"},
                   {"Code": "03.1.3.2", "Description": "Clothing accessories (SD)"}
               ]},
              {"Code": "03.1.4", "Description": "Cleaning, repair, tailoring and hire of clothing (S)",
               "Subcategories": [
                   {"Code": "03.1.4.1", "Description": "Cleaning of clothing (S)"},
                   {"Code": "03.1.4.2", "Description": "Repair, tailoring and hire of clothing (S)"}
               ]}
          ]},
         {"Code": "03.2", "Description": "Footwear",
          "Subcategories": [
              {"Code": "03.2.1", "Description": "Shoes and other footwear (SD)",
               "Subcategories": [
                   {"Code": "03.2.1.1", "Description": "Footwear for men (SD)"},
                   {"Code": "03.2.1.2", "Description": "Footwear for women (SD)"},
                   {"Code": "03.2.1.3", "Description": "Footwear for infants and children (SD)"}
               ]},
              {"Code": "03.2.2", "Description": "Cleaning, repair, and hire of footwear (S)",
               "Subcategories": [
                   {"Code": "03.2.2.0", "Description": "Cleaning, repair, and hire of footwear (S)"}
               ]}
          ]}
     ]}
]
  section_4 = [
    {"Code": "04", "Description": "Housing, water, electricity, gas and other fuels",
     "Subcategories": [
         {"Code": "04.1", "Description": "Actual rentals for housing",
          "Subcategories": [
              {"Code": "04.1.1", "Description": "Actual rentals paid by tenants for main residence (S)",
               "Subcategories": [
                   {"Code": "04.1.1.0", "Description": "Actual rentals paid by tenants for main residence (S)"}
               ]},
              {"Code": "04.1.2", "Description": "Other actual rentals (S)",
               "Subcategories": [
                   {"Code": "04.1.2.1", "Description": "Actual rentals paid by tenants for secondary residences (S)"},
                   {"Code": "04.1.2.2", "Description": "Garage rentals and other rentals paid by tenants (S)"}
               ]}
          ]},
         {"Code": "04.2", "Description": "Imputed rentals for housing",
          "Subcategories": [
              {"Code": "04.2.1", "Description": "Imputed rentals of owner-occupiers for main residence (S)",
               "Subcategories": [
                   {"Code": "04.2.1.0", "Description": "Imputed rentals of owner-occupiers for main residence (S)"}
               ]},
              {"Code": "04.2.2", "Description": "Other imputed rentals (S)",
               "Subcategories": [
                   {"Code": "04.2.2.0", "Description": "Other imputed rentals (S)"}
               ]}
          ]},
         {"Code": "04.3", "Description": "Maintenance, repair and security of the dwelling",
          "Subcategories": [
              {"Code": "04.3.1", "Description": "Security equipment and materials for the maintenance and repair of the dwelling (ND)",
               "Subcategories": [
                   {"Code": "04.3.1.1", "Description": "Materials for the maintenance and repair of the dwelling (ND)"},
                   {"Code": "04.3.1.2", "Description": "Security equipment (SD)"}
               ]},
              {"Code": "04.3.2", "Description": "Services for the maintenance, repair and security of the dwelling (S)",
               "Subcategories": [
                   {"Code": "04.3.2.0", "Description": "Services for the maintenance, repair and security of the dwelling (S)"}
               ]}
          ]},
         {"Code": "04.4", "Description": "Water supply and miscellaneous services relating to the dwelling",
          "Subcategories": [
              {"Code": "04.4.1", "Description": "Water supply (ND)",
               "Subcategories": [
                   {"Code": "04.4.1.1", "Description": "Water supply through network systems (ND)"},
                   {"Code": "04.4.1.2", "Description": "Water supply through other systems (ND)"}
               ]},
              {"Code": "04.4.2", "Description": "Refuse collection (S)",
               "Subcategories": [
                   {"Code": "04.4.2.0", "Description": "Refuse collection (S)"}
               ]},
              {"Code": "04.4.3", "Description": "Sewage collection (S)",
               "Subcategories": [
                   {"Code": "04.4.3.1", "Description": "Sewage collection through sewer systems (S)"},
                   {"Code": "04.4.3.2", "Description": "Sewage collection through onsite sanitation systems (S)"}
               ]},
              {"Code": "04.4.4", "Description": "Other services relating to the dwelling n.e.c. (S)",
               "Subcategories": [
                   {"Code": "04.4.4.1", "Description": "Maintenance charges in multi-occupied buildings (S)"},
                   {"Code": "04.4.4.9", "Description": "Other services related to dwelling (S)"}
               ]}
          ]},
         {"Code": "04.5", "Description": "Electricity, gas and other fuels",
          "Subcategories": [
              {"Code": "04.5.1", "Description": "Electricity (ND)",
               "Subcategories": [
                   {"Code": "04.5.1.0", "Description": "Electricity (ND)"}
               ]},
              {"Code": "04.5.2", "Description": "Gas (ND)",
               "Subcategories": [
                   {"Code": "04.5.2.1", "Description": "Natural gas through networks (ND)"},
                   {"Code": "04.5.2.2", "Description": "Liquefied hydrocarbons (ND)"}
               ]},
              {"Code": "04.5.3", "Description": "Liquid fuels (ND)",
               "Subcategories": [
                   {"Code": "04.5.3.0", "Description": "Liquid fuels (ND)"}
               ]},
              {"Code": "04.5.4", "Description": "Solid fuels (ND)",
               "Subcategories": [
                   {"Code": "04.5.4.1", "Description": "Coal, coal briquettes and peat (ND)"},
                   {"Code": "04.5.4.2", "Description": "Wood fuel, including pellets and briquettes (ND)"},
                   {"Code": "04.5.4.3", "Description": "Charcoal (ND)"},
                   {"Code": "04.5.4.9", "Description": "Other solid fuels (ND)"}
               ]},
              {"Code": "04.5.5", "Description": "Other energy for heating and cooling (ND)",
               "Subcategories": [
                   {"Code": "04.5.5.0", "Description": "Other energy for heating and cooling (ND)"}
               ]}
          ]}
     ]}
]
  section_5 = [
    {"Code": "05", "Description": "Furnishings, household equipment and routine household maintenance",
     "Subcategories": [
         {"Code": "05.1", "Description": "Furniture, furnishings, and loose carpets",
          "Subcategories": [
              {"Code": "05.1.1", "Description": "Furniture, furnishings and loose carpets (D)",
               "Subcategories": [
                   {"Code": "05.1.1.1", "Description": "Household furniture (D)"},
                   {"Code": "05.1.1.2", "Description": "Garden and camping furniture (D)"},
                   {"Code": "05.1.1.3", "Description": "Lighting equipment (D)"},
                   {"Code": "05.1.1.4", "Description": "Furnishings, loose carpets and rugs (D)"}
               ]},
              {"Code": "05.1.2", "Description": "Repair, installation and hire of furniture, furnishings and loose carpets (S)",
               "Subcategories": [
                   {"Code": "05.1.2.0", "Description": "Repair, installation and hire of furniture, furnishings and loose carpets (S)"}
               ]}
          ]},
         {"Code": "05.2", "Description": "Household textiles",
          "Subcategories": [
              {"Code": "05.2.1", "Description": "Household textiles (SD)",
               "Subcategories": [
                   {"Code": "05.2.1.1", "Description": "Furnishing fabrics and curtains (SD)"},
                   {"Code": "05.2.1.2", "Description": "Bed linen and bedding (SD)"},
                   {"Code": "05.2.1.3", "Description": "Table linen and bathroom linen (SD)"},
                   {"Code": "05.2.1.9", "Description": "Other household textiles (SD)"}
               ]},
              {"Code": "05.2.2", "Description": "Repair, hire and sewing services of household textiles (S)",
               "Subcategories": [
                   {"Code": "05.2.2.0", "Description": "Repair, hire and sewing services of household textiles (S)"}
               ]}
          ]},
         {"Code": "05.3", "Description": "Household appliances",
          "Subcategories": [
              {"Code": "05.3.1", "Description": "Major household appliances, whether electric or not (D)",
               "Subcategories": [
                   {"Code": "05.3.1.1", "Description": "Major kitchen appliances (D)"},
                   {"Code": "05.3.1.2", "Description": "Major laundry appliances (D)"},
                   {"Code": "05.3.1.3", "Description": "Heaters, air conditioners (D)"},
                   {"Code": "05.3.1.4", "Description": "Cleaning equipment (D)"},
                   {"Code": "05.3.1.9", "Description": "Other major household appliances (D)"}
               ]},
              {"Code": "05.3.2", "Description": "Small household appliances (SD)",
               "Subcategories": [
                   {"Code": "05.3.2.1", "Description": "Small appliances for cooking and processing of food (SD)"},
                   {"Code": "05.3.2.2", "Description": "Small appliances for preparing beverages (SD)"},
                   {"Code": "05.3.2.9", "Description": "Other small household appliances (SD)"}
               ]},
              {"Code": "05.3.3", "Description": "Repair, installation and hire of household appliances (S)",
               "Subcategories": [
                   {"Code": "05.3.3.0", "Description": "Repair, installation and hire of household appliances (S)"}
               ]}
          ]},
         {"Code": "05.4", "Description": "Glassware, tableware and household utensils",
          "Subcategories": [
              {"Code": "05.4.0", "Description": "Glassware, tableware and household utensils (SD)",
               "Subcategories": [
                   {"Code": "05.4.0.1", "Description": "Glassware, crystal-ware, ceramic ware and chinaware (SD)"},
                   {"Code": "05.4.0.2", "Description": "Cutlery, flatware and silverware (SD)"},
                   {"Code": "05.4.0.3", "Description": "Kitchen utensils and articles (SD)"},
                   {"Code": "05.4.0.4", "Description": "Repair and hire of glassware, tableware and household utensils (S)"}
               ]}
          ]},
         {"Code": "05.5", "Description": "Tools and equipment for house and garden",
          "Subcategories": [
              {"Code": "05.5.1", "Description": "Motorized tools and equipment (D)",
               "Subcategories": [
                   {"Code": "05.5.1.0", "Description": "Motorized tools and equipment (D)"}
               ]},
              {"Code": "05.5.2", "Description": "Non-motorized tools and miscellaneous accessories (SD)",
               "Subcategories": [
                   {"Code": "05.5.2.1", "Description": "Non-motorized tools (SD)"},
                   {"Code": "05.5.2.2", "Description": "Miscellaneous accessories (SD)"}
               ]},
              {"Code": "05.5.3", "Description": "Repair and hire of motorized and non-motorized tools and equipment (S)",
               "Subcategories": [
                   {"Code": "05.5.3.0", "Description": "Repair and hire of motorized and non-motorized tools and equipment (S)"}
               ]}
          ]},
         {"Code": "05.6", "Description": "Goods and services for routine household maintenance",
          "Subcategories": [
              {"Code": "05.6.1", "Description": "Non-durable household goods (ND)",
               "Subcategories": [
                   {"Code": "05.6.1.1", "Description": "Household cleaning and maintenance products (ND)"},
                   {"Code": "05.6.1.9", "Description": "Other non-durable household goods (ND)"}
               ]},
              {"Code": "05.6.2", "Description": "Domestic services and household services (S)",
               "Subcategories": [
                   {"Code": "05.6.2.1", "Description": "Domestic services by paid staff (S)"},
                   {"Code": "05.6.2.9", "Description": "Other household services (S)"}
               ]}
          ]}
     ]}
]
  section_6 = [
    {"Code": "06", "Description": "Health",
     "Subcategories": [
         {"Code": "06.1", "Description": "Medicines and health products",
          "Subcategories": [
              {"Code": "06.1.1", "Description": "Medicines (ND)",
               "Subcategories": [
                   {"Code": "06.1.1.1", "Description": "Medicines, vaccines and other pharmaceutical preparations (ND)"},
                   {"Code": "06.1.1.2", "Description": "Herbal medicines and homeopathic products (ND)"}
               ]},
              {"Code": "06.1.2", "Description": "Medical products (ND)",
               "Subcategories": [
                   {"Code": "06.1.2.1", "Description": "Medical diagnostic products (ND)"},
                   {"Code": "06.1.2.2", "Description": "Prevention and protective devices (ND)"},
                   {"Code": "06.1.2.3", "Description": "Treatment devices for personal use (ND)"}
               ]},
              {"Code": "06.1.3", "Description": "Assistive products (D)",
               "Subcategories": [
                   {"Code": "06.1.3.1", "Description": "Assistive products for vision (D)"},
                   {"Code": "06.1.3.2", "Description": "Assistive products for hearing and communication (D)"},
                   {"Code": "06.1.3.3", "Description": "Assistive products for mobility and daily living (D)"}
               ]},
              {"Code": "06.1.4", "Description": "Repair, rental and maintenance of medical and assistive products (S)",
               "Subcategories": [
                   {"Code": "06.1.4.0", "Description": "Repair, rental and maintenance of medical and assistive products (S)"}
               ]}
          ]},
         {"Code": "06.2", "Description": "Outpatient care services",
          "Subcategories": [
              {"Code": "06.2.1", "Description": "Preventive care services (S)",
               "Subcategories": [
                   {"Code": "06.2.1.1", "Description": "Immunization services (S)"},
                   {"Code": "06.2.1.9", "Description": "Other preventive services (S)"}
               ]},
              {"Code": "06.2.2", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "06.2.2.1", "Description": "Dental preventive services (S)"},
                   {"Code": "06.2.2.9", "Description": "Other outpatient dental services (S)"}
               ]},
              {"Code": "06.2.3", "Description": "Other outpatient care services (S)",
               "Subcategories": [
                   {"Code": "06.2.3.1", "Description": "Outpatient curative and rehabilitative services (S)"},
                   {"Code": "06.2.3.2", "Description": "Outpatient long-term care services (S)"}
               ]}
          ]},
         {"Code": "06.3", "Description": "Inpatient care services",
          "Subcategories": [
              {"Code": "06.3.1", "Description": "Inpatient curative and rehabilitative services (S)",
               "Subcategories": [
                   {"Code": "06.3.1.0", "Description": "Inpatient curative and rehabilitative services (S)"}
               ]},
              {"Code": "06.3.2", "Description": "Inpatient long-term care services (S)",
               "Subcategories": [
                   {"Code": "06.3.2.0", "Description": "Inpatient long-term care services (S)"}
               ]}
          ]},
         {"Code": "06.4", "Description": "Other health services",
          "Subcategories": [
              {"Code": "06.4.1", "Description": "Diagnostic imaging services and medical laboratory services (S)",
               "Subcategories": [
                   {"Code": "06.4.1.0", "Description": "Diagnostic imaging services and medical laboratory services (S)"}
               ]},
              {"Code": "06.4.2", "Description": "Patient emergency transportation services and emergency rescue (S)",
               "Subcategories": [
                   {"Code": "06.4.2.0", "Description": "Patient emergency transportation services and emergency rescue (S)"}
               ]}
          ]}
     ]}
]
  section_7 = [
    {"Code": "07", "Description": "Transport",
     "Subcategories": [
         {"Code": "07.1", "Description": "Purchase of vehicles",
          "Subcategories": [
              {"Code": "07.1.1", "Description": "Motor cars (D)",
               "Subcategories": [
                   {"Code": "07.1.1.1", "Description": "New motor cars (D)"},
                   {"Code": "07.1.1.2", "Description": "Second-hand motor cars (D)"}
               ]},
              {"Code": "07.1.2", "Description": "Motorcycles (D)",
               "Subcategories": [
                   {"Code": "07.1.2.0", "Description": "Motorcycles (D)"}
               ]},
              {"Code": "07.1.3", "Description": "Bicycles (D)",
               "Subcategories": [
                   {"Code": "07.1.3.0", "Description": "Bicycles (D)"}
               ]},
              {"Code": "07.1.4", "Description": "Animal drawn vehicles (D)",
               "Subcategories": [
                   {"Code": "07.1.4.0", "Description": "Animal drawn vehicles (D)"}
               ]}
          ]},
         {"Code": "07.2", "Description": "Operation of personal transport equipment",
          "Subcategories": [
              {"Code": "07.2.1", "Description": "Parts and accessories for personal transport equipment (SD)",
               "Subcategories": [
                   {"Code": "07.2.1.1", "Description": "Tyres (SD)"},
                   {"Code": "07.2.1.2", "Description": "Parts for personal transport equipment (SD)"},
                   {"Code": "07.2.1.3", "Description": "Accessories for personal transport equipment (SD)"}
               ]},
              {"Code": "07.2.2", "Description": "Fuels and lubricants for personal transport equipment (ND)",
               "Subcategories": [
                   {"Code": "07.2.2.1", "Description": "Diesel (ND)"},
                   {"Code": "07.2.2.2", "Description": "Petrol (ND)"},
                   {"Code": "07.2.2.3", "Description": "Other fuels for personal transport equipment (ND)"},
                   {"Code": "07.2.2.4", "Description": "Lubricants (ND)"}
               ]},
              {"Code": "07.2.3", "Description": "Maintenance and repair of personal transport equipment (S)",
               "Subcategories": [
                   {"Code": "07.2.3.0", "Description": "Maintenance and repair of personal transport equipment (S)"}
               ]},
              {"Code": "07.2.4", "Description": "Other services in respect of personal transport equipment (S)",
               "Subcategories": [
                   {"Code": "07.2.4.1", "Description": "Services for parking (S)"},
                   {"Code": "07.2.4.2", "Description": "Toll facilities (S)"},
                   {"Code": "07.2.4.3", "Description": "Driving lessons, tests, licences, and roadworthiness tests (S)"},
                   {"Code": "07.2.4.4", "Description": "Hire of personal transport equipment without driver (S)"}
               ]}
          ]},
         {"Code": "07.3", "Description": "Passenger transport services",
          "Subcategories": [
              {"Code": "07.3.1", "Description": "Passenger transport by railway (S)",
               "Subcategories": [
                   {"Code": "07.3.1.1", "Description": "Passenger transport by train (S)"},
                   {"Code": "07.3.1.2", "Description": "Passenger transport by rapid transit and tram (S)"}
               ]},
              {"Code": "07.3.2", "Description": "Passenger transport by road (S)",
               "Subcategories": [
                   {"Code": "07.3.2.1", "Description": "Passenger transport by bus and coach (S)"},
                   {"Code": "07.3.2.2", "Description": "Passenger transport by taxi and hired car with driver (S)"},
                   {"Code": "07.3.2.3", "Description": "Passenger transport for students to and from school (S)"},
                   {"Code": "07.3.2.9", "Description": "Other passenger transport by road (S)"}
               ]},
              {"Code": "07.3.3", "Description": "Passenger transport by air (S)",
               "Subcategories": [
                   {"Code": "07.3.3.1", "Description": "Passenger transport by air, domestic (S)"},
                   {"Code": "07.3.3.2", "Description": "Passenger transport by air, international (S)"}
               ]},
              {"Code": "07.3.4", "Description": "Passenger transport by sea and inland waterway (S)",
               "Subcategories": [
                   {"Code": "07.3.4.0", "Description": "Passenger transport by sea and inland waterway (S)"}
               ]},
              {"Code": "07.3.5", "Description": "Combined passenger transport (S)",
               "Subcategories": [
                   {"Code": "07.3.5.0", "Description": "Combined passenger transport (S)"}
               ]},
              {"Code": "07.3.6", "Description": "Other purchased transport services (S)",
               "Subcategories": [
                   {"Code": "07.3.6.0", "Description": "Other purchased transport services (S)"}
               ]}
          ]},
         {"Code": "07.4", "Description": "Transport services of goods",
          "Subcategories": [
              {"Code": "07.4.1", "Description": "Postal and courier services (S)",
               "Subcategories": [
                   {"Code": "07.4.1.1", "Description": "Letter handling services (S)"},
                   {"Code": "07.4.1.2", "Description": "Courier and parcel delivery services (S)"}
               ]},
              {"Code": "07.4.9", "Description": "Other transport of goods (S)",
               "Subcategories": [
                   {"Code": "07.4.9.1", "Description": "Removal and storage services (S)"},
                   {"Code": "07.4.9.2", "Description": "Delivery of goods (S)"}
               ]}
          ]}
     ]}
]
  section_8 = [
    {"Code": "08", "Description": "Information and communication",
     "Subcategories": [
         {"Code": "08.1", "Description": "Information and communication equipment",
          "Subcategories": [
              {"Code": "08.1.1", "Description": "Fixed telephone equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.1.0", "Description": "Fixed telephone equipment (D)"}
               ]},
              {"Code": "08.1.2", "Description": "Mobile telephone equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.2.0", "Description": "Mobile telephone equipment (D)"}
               ]},
              {"Code": "08.1.3", "Description": "Information processing equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.3.1", "Description": "Computers, laptops and tablets (D)"},
                   {"Code": "08.1.3.2", "Description": "Peripheral equipment and its consumable components (D)"}
               ]},
              {"Code": "08.1.4", "Description": "Equipment for the reception, recording and reproduction of sound and vision (D)",
               "Subcategories": [
                   {"Code": "08.1.4.0", "Description": "Equipment for the reception, recording and reproduction of sound and vision (D)"}
               ]},
              {"Code": "08.1.5", "Description": "Unrecorded recording media (SD)",
               "Subcategories": [
                   {"Code": "08.1.5.0", "Description": "Unrecorded recording media (SD)"}
               ]},
              {"Code": "08.1.9", "Description": "Other information and communication equipment and accessories (D)",
               "Subcategories": [
                   {"Code": "08.1.9.1", "Description": "Other information and communication equipment (D)"},
                   {"Code": "08.1.9.2", "Description": "Other information and communication accessories (SD)"}
               ]}
          ]},
         {"Code": "08.2", "Description": "Software excluding games",
          "Subcategories": [
              {"Code": "08.2.0", "Description": "Software (S)",
               "Subcategories": [
                   {"Code": "08.2.0.0", "Description": "Software (S)"}
               ]}
          ]},
         {"Code": "08.3", "Description": "Information and communication services",
          "Subcategories": [
              {"Code": "08.3.1", "Description": "Fixed communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.1.0", "Description": "Fixed communication services (S)"}
               ]},
              {"Code": "08.3.2", "Description": "Mobile communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.2.0", "Description": "Mobile communication services (S)"}
               ]},
              {"Code": "08.3.3", "Description": "Internet access provision services and net storage services (S)",
               "Subcategories": [
                   {"Code": "08.3.3.0", "Description": "Internet access provision services and net storage services (S)"}
               ]},
              {"Code": "08.3.4", "Description": "Bundled telecommunication services (S)",
               "Subcategories": [
                   {"Code": "08.3.4.0", "Description": "Bundled telecommunication services (S)"}
               ]},
              {"Code": "08.3.5", "Description": "Repair and rental of information and communication equipment (S)",
               "Subcategories": [
                   {"Code": "08.3.5.0", "Description": "Repair and rental of information and communication equipment (S)"}
               ]},
              {"Code": "08.3.9", "Description": "Other information and communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.9.1", "Description": "TV and radio licences and fees (S)"},
                   {"Code": "08.3.9.2", "Description": "Subscription to audio-visual content, streaming services and rentals of audio-visual content (S)"},
                   {"Code": "08.3.9.9", "Description": "Other information and communication services (S)"}
               ]}
          ]}
     ]}
]
  section_9 = [
    {"Code": "09", "Description": "Recreation, sport and culture",
     "Subcategories": [
         {"Code": "09.1", "Description": "Recreational durables",
          "Subcategories": [
              {"Code": "09.1.1", "Description": "Photographic and cinematographic equipment and optical instruments (D)",
               "Subcategories": [
                   {"Code": "09.1.1.1", "Description": "Cameras (D)"},
                   {"Code": "09.1.1.2", "Description": "Accessories for photographic and cinematographic equipment (D)"},
                   {"Code": "09.1.1.3", "Description": "Optical instruments (D)"}
               ]},
              {"Code": "09.1.2", "Description": "Major durables for recreation (D)",
               "Subcategories": [
                   {"Code": "09.1.2.1", "Description": "Camper vans, caravans and trailers (D)"},
                   {"Code": "09.1.2.2", "Description": "Aeroplanes, microlight aircraft, gliders, hang gliders and hot-air balloons (D)"},
                   {"Code": "09.1.2.3", "Description": "Boats, yachts, outboard motors and other water sport equipment (D)"},
                   {"Code": "09.1.2.4", "Description": "Horses, ponies, camel and dromedaries and accessories (D)"},
                   {"Code": "09.1.2.9", "Description": "Other major durables for recreation (D)"}
               ]}
          ]},
         {"Code": "09.2", "Description": "Other recreational goods",
          "Subcategories": [
              {"Code": "09.2.1", "Description": "Games, toys and hobbies (SD)",
               "Subcategories": [
                   {"Code": "09.2.1.1", "Description": "Video game computers, game consoles, game apps and software (SD)"},
                   {"Code": "09.2.1.2", "Description": "Other games, toys and hobbies (SD)"},
                   {"Code": "09.2.1.3", "Description": "Celebration articles (ND)"}
               ]},
              {"Code": "09.2.2", "Description": "Equipment for sport, camping and open-air recreation (SD)",
               "Subcategories": [
                   {"Code": "09.2.2.1", "Description": "Equipment for sport (SD)"},
                   {"Code": "09.2.2.2", "Description": "Equipment for camping and open-air recreation (SD)"}
               ]}
          ]},
         {"Code": "09.3", "Description": "Garden products and pets",
          "Subcategories": [
              {"Code": "09.3.1", "Description": "Garden products, plants and flowers (ND)",
               "Subcategories": [
                   {"Code": "09.3.1.1", "Description": "Garden products (ND)"},
                   {"Code": "09.3.1.2", "Description": "Plants, seeds and flowers (ND)"}
               ]},
              {"Code": "09.3.2", "Description": "Pets and products for pets (ND)",
               "Subcategories": [
                   {"Code": "09.3.2.1", "Description": "Purchase of pets (ND)"},
                   {"Code": "09.3.2.2", "Description": "Products for pets and other household animals (ND)"}
               ]}
          ]},
         {"Code": "09.4", "Description": "Recreational services",
          "Subcategories": [
              {"Code": "09.4.1", "Description": "Hire and repair of photographic and cinematographic equipment and optical instruments (S)",
               "Subcategories": [
                   {"Code": "09.4.1.0", "Description": "Hire and repair of photographic and cinematographic equipment and optical instruments (S)"}
               ]},
              {"Code": "09.4.2", "Description": "Hire, maintenance and repair of major durables for recreation (S)",
               "Subcategories": [
                   {"Code": "09.4.2.1", "Description": "Hire, maintenance and repair of camper vans and caravans (S)"},
                   {"Code": "09.4.2.2", "Description": "Hire, maintenance and repair of other major durables for recreation (S)"}
               ]},
              {"Code": "09.4.3", "Description": "Hire and repair of games, toys and hobbies (S)",
               "Subcategories": [
                   {"Code": "09.4.3.1", "Description": "Rental of game software and subscription to online games (S)"},
                   {"Code": "09.4.3.2", "Description": "Rental and repair of games, toys and hobbies (S)"}
               ]},
              {"Code": "09.4.4", "Description": "Hire and repair of equipment for sport, camping and open-air recreation (S)",
               "Subcategories": [
                   {"Code": "09.4.4.0", "Description": "Hire and repair of equipment for sport, camping and open-air recreation (S)"}
               ]},
              {"Code": "09.4.5", "Description": "Veterinary and other services for pets (S)",
               "Subcategories": [
                   {"Code": "09.4.5.0", "Description": "Veterinary and other services for pets (S)"}
               ]},
              {"Code": "09.4.6", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "09.4.6.1", "Description": "Recreational and leisure services (S)"},
                   {"Code": "09.4.6.2", "Description": "Sporting services - practice (S)"},
                   {"Code": "09.4.6.3", "Description": "Sporting services - attendance (S)"}
               ]},
              {"Code": "09.4.7", "Description": "Games of chance (S)",
               "Subcategories": [
                   {"Code": "09.4.7.0", "Description": "Games of chance (S)"}
               ]}
          ]},
         {"Code": "09.5", "Description": "Cultural goods",
          "Subcategories": [
              {"Code": "09.5.1", "Description": "Musical instruments (D)",
               "Subcategories": [
                   {"Code": "09.5.1.0", "Description": "Musical instruments (D)"}
               ]},
              {"Code": "09.5.2", "Description": "Audio-visual media (SD)",
               "Subcategories": [
                   {"Code": "09.5.2.0", "Description": "Audio-visual media (SD)"}
               ]}
          ]},
         {"Code": "09.6", "Description": "Cultural services",
          "Subcategories": [
              {"Code": "09.6.1", "Description": "Services provided by cinemas, theatres and concert venues (S)",
               "Subcategories": [
                   {"Code": "09.6.1.0", "Description": "Services provided by cinemas, theatres and concert venues (S)"}
               ]},
              {"Code": "09.6.2", "Description": "Services provided by museums, libraries, and cultural sites (S)",
               "Subcategories": [
                   {"Code": "09.6.2.0", "Description": "Services provided by museums, libraries, and cultural sites (S)"}
               ]},
              {"Code": "09.6.3", "Description": "Photographic services (S)",
               "Subcategories": [
                   {"Code": "09.6.3.0", "Description": "Photographic services (S)"}
               ]},
              {"Code": "09.6.9", "Description": "Other cultural services (S)",
               "Subcategories": [
                   {"Code": "09.6.9.0", "Description": "Other cultural services (S)"}
               ]}
          ]},
         {"Code": "09.7", "Description": "Newspapers, books and stationery",
          "Subcategories": [
              {"Code": "09.7.1", "Description": "Books (SD)",
               "Subcategories": [
                   {"Code": "09.7.1.1", "Description": "Educational and text books (SD)"},
                   {"Code": "09.7.1.9", "Description": "Other books (SD)"}
               ]},
              {"Code": "09.7.2", "Description": "Newspapers and periodicals (ND)",
               "Subcategories": [
                   {"Code": "09.7.2.1", "Description": "Newspapers (ND)"},
                   {"Code": "09.7.2.2", "Description": "Magazines and periodicals (ND)"}
               ]},
              {"Code": "09.7.3", "Description": "Miscellaneous printed matter (ND)",
               "Subcategories": [
                   {"Code": "09.7.3.0", "Description": "Miscellaneous printed matter (ND)"}
               ]},
              {"Code": "09.7.4", "Description": "Stationery and drawing materials (ND)",
               "Subcategories": [
                   {"Code": "09.7.4.0", "Description": "Stationery and drawing materials (ND)"}
               ]}
          ]},
         {"Code": "09.8", "Description": "Package holidays",
          "Subcategories": [
              {"Code": "09.8.0", "Description": "Package holidays (S)",
               "Subcategories": [
                   {"Code": "09.8.0.0", "Description": "Package holidays (S)"}
               ]}
          ]}
     ]}
]
  section_10 = [
    {"Code": "10", "Description": "Education services",
     "Subcategories": [
         {"Code": "10.1", "Description": "Early childhood and primary education",
          "Subcategories": [
              {"Code": "10.1.0", "Description": "Early childhood and primary education (S)",
               "Subcategories": [
                   {"Code": "10.1.0.1", "Description": "Early childhood education (S)"},
                   {"Code": "10.1.0.2", "Description": "Primary education (S)"}
               ]}
          ]},
         {"Code": "10.2", "Description": "Secondary education",
          "Subcategories": [
              {"Code": "10.2.0", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "10.2.0.0", "Description": "Secondary education (S)"}
               ]}
          ]},
         {"Code": "10.3", "Description": "Post-secondary non-tertiary education",
          "Subcategories": [
              {"Code": "10.3.0", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "10.3.0.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]}
          ]},
         {"Code": "10.4", "Description": "Tertiary education",
          "Subcategories": [
              {"Code": "10.4.0", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "10.4.0.0", "Description": "Tertiary education (S)"}
               ]}
          ]},
         {"Code": "10.5", "Description": "Education not defined by level",
          "Subcategories": [
              {"Code": "10.5.0", "Description": "Education not defined by level (S)",
               "Subcategories": [
                   {"Code": "10.5.0.1", "Description": "Tutoring (S)"},
                   {"Code": "10.5.0.9", "Description": "Other education not defined by level (S)"}
               ]}
          ]}
     ]}
]
  section_11 = [
    {"Code": "11", "Description": "Restaurants and accommodation services",
     "Subcategories": [
         {"Code": "11.1", "Description": "Food and beverage serving services",
          "Subcategories": [
              {"Code": "11.1.1", "Description": "Restaurants, cafés and the like (S)",
               "Subcategories": [
                   {"Code": "11.1.1.1", "Description": "Restaurants, cafés and the like – with full service (S)"},
                   {"Code": "11.1.1.2", "Description": "Restaurants, cafés and the like – with limited service (S)"}
               ]},
              {"Code": "11.1.2", "Description": "Canteens, cafeterias and refectories (S)",
               "Subcategories": [
                   {"Code": "11.1.2.1", "Description": "Canteens, cafeterias of universities, schools, and kindergartens (S)"},
                   {"Code": "11.1.2.9", "Description": "Other canteens, cafeterias and refectories (S)"}
               ]}
          ]},
         {"Code": "11.2", "Description": "Accommodation services",
          "Subcategories": [
              {"Code": "11.2.0", "Description": "Accommodation services (S)",
               "Subcategories": [
                   {"Code": "11.2.0.1", "Description": "Hotels, motels, inns and similar accommodation services (S)"},
                   {"Code": "11.2.0.2", "Description": "Holiday centres, camping sites, youth hostels and similar accommodation services (S)"},
                   {"Code": "11.2.0.3", "Description": "Accommodation services of boarding schools, universities and other educational establishments (S)"},
                   {"Code": "11.2.0.9", "Description": "Other accommodation services (S)"}
               ]}
          ]}
     ]}
]
  section_12 = [
    {"Code": "12", "Description": "Insurance and financial services",
     "Subcategories": [
         {"Code": "12.1", "Description": "Insurance",
          "Subcategories": [
              {"Code": "12.1.1", "Description": "Life and accident insurance (S)",
               "Subcategories": [
                   {"Code": "12.1.1.0", "Description": "Life and accident insurance (S)"}
               ]},
              {"Code": "12.1.2", "Description": "Insurance connected with health (S)",
               "Subcategories": [
                   {"Code": "12.1.2.0", "Description": "Insurance connected with health (S)"}
               ]},
              {"Code": "12.1.3", "Description": "Insurance connected with the dwelling (S)",
               "Subcategories": [
                   {"Code": "12.1.3.0", "Description": "Insurance connected with the dwelling (S)"}
               ]},
              {"Code": "12.1.4", "Description": "Insurance connected with transport (S)",
               "Subcategories": [
                   {"Code": "12.1.4.1", "Description": "Personal transport insurance (S)"},
                   {"Code": "12.1.4.2", "Description": "Travel insurance (S)"}
               ]},
              {"Code": "12.1.9", "Description": "Other insurance (S)",
               "Subcategories": [
                   {"Code": "12.1.9.0", "Description": "Other insurance (S)"}
               ]}
          ]},
         {"Code": "12.2", "Description": "Financial services",
          "Subcategories": [
              {"Code": "12.2.1", "Description": "Financial intermediation services indirectly measured (S)",
               "Subcategories": [
                   {"Code": "12.2.1.0", "Description": "Financial intermediation services indirectly measured (S)"}
               ]},
              {"Code": "12.2.2", "Description": "Explicit charges by deposit-taking corporations (S)",
               "Subcategories": [
                   {"Code": "12.2.2.0", "Description": "Explicit charges by deposit-taking corporations (S)"}
               ]},
              {"Code": "12.2.9", "Description": "Other financial services (S)",
               "Subcategories": [
                   {"Code": "12.2.9.1", "Description": "Remittances fees (S)"},
                   {"Code": "12.2.9.9", "Description": "Other financial services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_13 = [
    {"Code": "13", "Description": "Personal care, social protection, and miscellaneous goods and services",
     "Subcategories": [
         {"Code": "13.1", "Description": "Personal care",
          "Subcategories": [
              {"Code": "13.1.1", "Description": "Electric appliances for personal care (SD)",
               "Subcategories": [
                   {"Code": "13.1.1.1", "Description": "Electric appliances for personal care (SD)"},
                   {"Code": "13.1.1.2", "Description": "Repair of electric appliances for personal care (S)"}
               ]},
              {"Code": "13.1.2", "Description": "Other appliances, articles, and products for personal care (ND)",
               "Subcategories": [
                   {"Code": "13.1.2.0", "Description": "Other appliances, articles, and products for personal care (ND)"}
               ]},
              {"Code": "13.1.3", "Description": "Hairdressing salons and personal grooming establishments (S)",
               "Subcategories": [
                   {"Code": "13.1.3.1", "Description": "Hairdressing (S)"},
                   {"Code": "13.1.3.2", "Description": "Personal grooming treatments (S)"}
               ]}
          ]},
         {"Code": "13.2", "Description": "Other personal effects",
          "Subcategories": [
              {"Code": "13.2.1", "Description": "Jewellery and watches (D)",
               "Subcategories": [
                   {"Code": "13.2.1.1", "Description": "Jewellery and watches (D)"},
                   {"Code": "13.2.1.2", "Description": "Repair and hire of jewellery, clocks, and watches (S)"}
               ]},
              {"Code": "13.2.2", "Description": "Devotional articles and articles for religious and ritual celebrations (SD)",
               "Subcategories": [
                   {"Code": "13.2.2.0", "Description": "Devotional articles and articles for religious and ritual celebrations (SD)"}
               ]},
              {"Code": "13.2.9", "Description": "Other personal effects n.e.c. (SD)",
               "Subcategories": [
                   {"Code": "13.2.9.1", "Description": "Travel goods and articles for babies and other personal effects n.e.c. (SD)"},
                   {"Code": "13.2.9.2", "Description": "Repair or hire of other personal effects n.e.c. (S)"}
               ]}
          ]},
         {"Code": "13.3", "Description": "Social protection",
          "Subcategories": [
              {"Code": "13.3.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "13.3.0.1", "Description": "Child care services (S)"},
                   {"Code": "13.3.0.2", "Description": "Non-medical retirement homes for elderly persons and residences for disabled persons (S)"},
                   {"Code": "13.3.0.3", "Description": "Services to maintain persons in their private homes (S)"},
                   {"Code": "13.3.0.9", "Description": "Other social protection services (S)"}
               ]}
          ]},
         {"Code": "13.9", "Description": "Other services",
          "Subcategories": [
              {"Code": "13.9.0", "Description": "Other services (S)",
               "Subcategories": [
                   {"Code": "13.9.0.1", "Description": "Prostitution (S)"},
                   {"Code": "13.9.0.2", "Description": "Religious services (S)"},
                   {"Code": "13.9.0.9", "Description": "Other services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_14 = [
    {"Code": "14", "Description": "Individual consumption expenditure of non-profit institutions serving households (NPISHs)",
     "Subcategories": [
         {"Code": "14.1", "Description": "Housing",
          "Subcategories": [
              {"Code": "14.1.0", "Description": "Housing (S)",
               "Subcategories": [
                   {"Code": "14.1.0.0", "Description": "Housing (S)"}
               ]}
          ]},
         {"Code": "14.2", "Description": "Health",
          "Subcategories": [
              {"Code": "14.2.1", "Description": "Pharmaceutical products (ND)",
               "Subcategories": [
                   {"Code": "14.2.1.0", "Description": "Pharmaceutical products (ND)"}
               ]},
              {"Code": "14.2.2", "Description": "Other medical products (ND)",
               "Subcategories": [
                   {"Code": "14.2.2.0", "Description": "Other medical products (ND)"}
               ]},
              {"Code": "14.2.3", "Description": "Therapeutic appliances and equipment (D)",
               "Subcategories": [
                   {"Code": "14.2.3.0", "Description": "Therapeutic appliances and equipment (D)"}
               ]},
              {"Code": "14.2.4", "Description": "Outpatient medical services (S)",
               "Subcategories": [
                   {"Code": "14.2.4.0", "Description": "Outpatient medical services (S)"}
               ]},
              {"Code": "14.2.5", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "14.2.5.0", "Description": "Outpatient dental services (S)"}
               ]},
              {"Code": "14.2.6", "Description": "Outpatient paramedical services (S)",
               "Subcategories": [
                   {"Code": "14.2.6.0", "Description": "Outpatient paramedical services (S)"}
               ]},
              {"Code": "14.2.7", "Description": "Hospital services (S)",
               "Subcategories": [
                   {"Code": "14.2.7.0", "Description": "Hospital services (S)"}
               ]},
              {"Code": "14.2.8", "Description": "Other health services (S)",
               "Subcategories": [
                   {"Code": "14.2.8.0", "Description": "Other health services (S)"}
               ]}
          ]},
         {"Code": "14.3", "Description": "Recreation and culture",
          "Subcategories": [
              {"Code": "14.3.1", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "14.3.1.0", "Description": "Recreational and sporting services (S)"}
               ]},
              {"Code": "14.3.2", "Description": "Cultural services (S)",
               "Subcategories": [
                   {"Code": "14.3.2.0", "Description": "Cultural services (S)"}
               ]}
          ]},
         {"Code": "14.4", "Description": "Education",
          "Subcategories": [
              {"Code": "14.4.1", "Description": "Pre-primary and primary education (S)",
               "Subcategories": [
                   {"Code": "14.4.1.0", "Description": "Pre-primary and primary education (S)"}
               ]},
              {"Code": "14.4.2", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "14.4.2.0", "Description": "Secondary education (S)"}
               ]},
              {"Code": "14.4.3", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "14.4.3.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]},
              {"Code": "14.4.4", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "14.4.4.0", "Description": "Tertiary education (S)"}
               ]},
              {"Code": "14.4.5", "Description": "Education not definable by level (S)",
               "Subcategories": [
                   {"Code": "14.4.5.0", "Description": "Education not definable by level (S)"}
               ]},
              {"Code": "14.4.6", "Description": "Other educational services (S)",
               "Subcategories": [
                   {"Code": "14.4.6.0", "Description": "Other educational services (S)"}
               ]}
          ]},
         {"Code": "14.5", "Description": "Social protection",
          "Subcategories": [
              {"Code": "14.5.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "14.5.0.0", "Description": "Social protection (S)"}
               ]}
          ]},
         {"Code": "14.6", "Description": "Other services",
          "Subcategories": [
              {"Code": "14.6.1", "Description": "Religion (S)",
               "Subcategories": [
                   {"Code": "14.6.1.0", "Description": "Religion (S)"}
               ]},
              {"Code": "14.6.2", "Description": "Political parties, labour, and professional organizations (S)",
               "Subcategories": [
                   {"Code": "14.6.2.0", "Description": "Political parties, labour, and professional organizations (S)"}
               ]},
              {"Code": "14.6.3", "Description": "Environmental protection (S)",
               "Subcategories": [
                   {"Code": "14.6.3.0", "Description": "Environmental protection (S)"}
               ]},
              {"Code": "14.6.4", "Description": "Services n.e.c. (S)",
               "Subcategories": [
                   {"Code": "14.6.4.0", "Description": "Services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_15 = [
    {"Code": "15", "Description": "Individual consumption expenditure of general government",
     "Subcategories": [
         {"Code": "15.1", "Description": "Housing",
          "Subcategories": [
              {"Code": "15.1.0", "Description": "Housing (S)",
               "Subcategories": [
                   {"Code": "15.1.0.0", "Description": "Housing (S)"}
               ]}
          ]},
         {"Code": "15.2", "Description": "Health",
          "Subcategories": [
              {"Code": "15.2.1", "Description": "Pharmaceutical products (ND)",
               "Subcategories": [
                   {"Code": "15.2.1.0", "Description": "Pharmaceutical products (ND)"}
               ]},
              {"Code": "15.2.2", "Description": "Other medical products (ND)",
               "Subcategories": [
                   {"Code": "15.2.2.0", "Description": "Other medical products (ND)"}
               ]},
              {"Code": "15.2.3", "Description": "Therapeutic appliances and equipment (D)",
               "Subcategories": [
                   {"Code": "15.2.3.0", "Description": "Therapeutic appliances and equipment (D)"}
               ]},
              {"Code": "15.2.4", "Description": "Outpatient medical services (S)",
               "Subcategories": [
                   {"Code": "15.2.4.0", "Description": "Outpatient medical services (S)"}
               ]},
              {"Code": "15.2.5", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "15.2.5.0", "Description": "Outpatient dental services (S)"}
               ]},
              {"Code": "15.2.6", "Description": "Outpatient paramedical services (S)",
               "Subcategories": [
                   {"Code": "15.2.6.0", "Description": "Outpatient paramedical services (S)"}
               ]},
              {"Code": "15.2.7", "Description": "Hospital services (S)",
               "Subcategories": [
                   {"Code": "15.2.7.0", "Description": "Hospital services (S)"}
               ]},
              {"Code": "15.2.8", "Description": "Public health services (S)",
               "Subcategories": [
                   {"Code": "15.2.8.0", "Description": "Public health services (S)"}
               ]}
          ]},
         {"Code": "15.3", "Description": "Recreation and culture",
          "Subcategories": [
              {"Code": "15.3.1", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "15.3.1.0", "Description": "Recreational and sporting services (S)"}
               ]},
              {"Code": "15.3.2", "Description": "Cultural services (S)",
               "Subcategories": [
                   {"Code": "15.3.2.0", "Description": "Cultural services (S)"}
               ]}
          ]},
         {"Code": "15.4", "Description": "Education",
          "Subcategories": [
              {"Code": "15.4.1", "Description": "Pre-primary and primary education (S)",
               "Subcategories": [
                   {"Code": "15.4.1.0", "Description": "Pre-primary and primary education (S)"}
               ]},
              {"Code": "15.4.2", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "15.4.2.0", "Description": "Secondary education (S)"}
               ]},
              {"Code": "15.4.3", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "15.4.3.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]},
              {"Code": "15.4.4", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "15.4.4.0", "Description": "Tertiary education (S)"}
               ]},
              {"Code": "15.4.5", "Description": "Education not definable by level (S)",
               "Subcategories": [
                   {"Code": "15.4.5.0", "Description": "Education not definable by level (S)"}
               ]},
              {"Code": "15.4.6", "Description": "Subsidiary services to education (S)",
               "Subcategories": [
                   {"Code": "15.4.6.0", "Description": "Subsidiary services to education (S)"}
               ]}
          ]},
         {"Code": "15.5", "Description": "Social protection",
          "Subcategories": [
              {"Code": "15.5.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "15.5.0.0", "Description": "Social protection (S)"}
               ]}
          ]}
     ]}
]


 #choose section based on hlsection response 
 # Create a dictionary mapping section codes to the corresponding lists
  section_mapping = {
        "01": section_1,
        "02": section_2,
        "03": section_3,
        "04": section_4,
        "05": section_5,
        "06": section_6,
        "07": section_7,
        "08": section_8,
        "09": section_9,
        "10": section_10,
        "11": section_11,
        "12": section_12,
        "13": section_13,
        "14": section_14,
        "15": section_15,
}
  
  #selecting list
  selected_section = section_mapping.get(hLSection)

  #getting the code of the subcatagory that it belongs to
  promptLowLevelCatagories="Please read the following catagory of coicop codes and determine which subcatagory their product falls under(respond with only the number of the catagory for example '04.2.1'):"+all_data
  for item in selected_section:
     strItem2=str(item)
     promptLowLevelCatagories+=strItem2

  coicop_finalcode = aiProcess(promptLowLevelCatagories)

  #method to find the description of that code  
  def find_description(coicop_list, code):
    for category in coicop_list:
        if category["Code"] == code:
            return category["Description"]
        if "Subcategories" in category:
            subcategory_description = find_description(category["Subcategories"], code)
            if subcategory_description:
                return subcategory_description
    return None
  
  
  description = find_description(selected_section, coicop_finalcode)
  return description



def findSIC_ofCompany(company_name, allData):
  


  #list of all the high level sections of sic codes
  sicIndex = ["Section A-Agriculture, Forestry and Fishing","Section B-Mining and Quarrying","Section C-Manufacturing","Section D-Electricity, gas, steam and air conditioning supply","Section E-Water supply, sewerage, waste management and remediation activities",
              "Section F-Construction","Section G-Wholesale and retail trade; repair of motor vehicles and motorcycles","Section H-Transportation and storage","Section I-Accommodation and food service activities","Section J-Information and communication",
              "Section K-Financial and insurance activities", "Section L-Real estate activities","Section M-Professional, scientific and technical activities","Section N-Administrative and support service activities",
              "Section O-Public administration and defence; compulsory social security","Section P-Education","Section Q-Human health and social work activities","Section R-Arts, entertainment and recreation","Section S-Other service activities",
              "Section T-Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use", "Section U-Activities of extraterritorial organisations and bodies"]

  promptHighLevelSection="Based on the information you have recieved"+allData+", which of the following catagories includes the company "+company_name+"? Respond ONLY with the uppercase letter of the section that it falls under(for example 'F') :"

  for item in sicIndex:
     promptHighLevelSection+="\n"+item  

  sectionResponse=aiProcess(promptHighLevelSection)
  print(sectionResponse)
  #lists for all of the sections and their respective codes
  A = [
        ["01110", "Growing of cereals (except rice), leguminous crops and oil seeds"],
        ["01120", "Growing of rice"],
        ["01130", "Growing of vegetables and melons, roots and tubers"],
        ["01140", "Growing of sugar cane"],
        ["01150", "Growing of tobacco"],
        ["01160", "Growing of fibre crops"],
        ["01190", "Growing of other non-perennial crops"],
        ["01210", "Growing of grapes"],
        ["01220", "Growing of tropical and subtropical fruits"],
        ["01230", "Growing of citrus fruits"],
        ["01240", "Growing of pome fruits and stone fruits"],
        ["01250", "Growing of other tree and bush fruits and nuts"],
        ["01260", "Growing of oleaginous fruits"],
        ["01270", "Growing of beverage crops"],
        ["01280", "Growing of spices, aromatic, drug and pharmaceutical crops"],
        ["01290", "Growing of other perennial crops"],
        ["01300", "Plant propagation"],
        ["01410", "Raising of dairy cattle"],
        ["01420", "Raising of other cattle and buffaloes"],
        ["01430", "Raising of horses and other equines"],
        ["01440", "Raising of camels and camelids"],
        ["01450", "Raising of sheep and goats"],
        ["01460", "Raising of swine/pigs"],
        ["01470", "Raising of poultry"],
        ["01490", "Raising of other animals"],
        ["01500", "Mixed farming"],
        ["01610", "Support activities for crop production"],
        ["01621", "Farm animal boarding and care"],
        ["01629", "Support activities for animal production (other than farm animal boarding and care) n.e.c."],
        ["01630", "Post-harvest crop activities"],
        ["01640", "Seed processing for propagation"],
        ["01700", "Hunting, trapping and related service activities"],
        ["02100", "Silviculture and other forestry activities"],
        ["02200", "Logging"],
        ["02300", "Gathering of wild growing non-wood products"],
        ["02400", "Support services to forestry"],
        ["03110", "Marine fishing"],
        ["03120", "Freshwater fishing"],
        ["03210", "Marine aquaculture"],
        ["03220", "Freshwater aquaculture"]
    ]
  B = [
        ["05101", "Deep coal mines"],
        ["05102", "Open cast coal working"],
        ["05200", "Mining of lignite"],
        ["06100", "Extraction of crude petroleum"],
        ["06200", "Extraction of natural gas"],
        ["07100", "Mining of iron ores"],
        ["07210", "Mining of uranium and thorium ores"],
        ["07290", "Mining of other non-ferrous metal ores"],
        ["08110", "Quarrying of ornamental and building stone, limestone, gypsum, chalk and slate"],
        ["08120", "Operation of gravel and sand pits; mining of clays and kaolin"],
        ["08910", "Mining of chemical and fertilizer minerals"],
        ["08920", "Extraction of peat"],
        ["08930", "Extraction of salt"],
        ["08990", "Other mining and quarrying n.e.c."],
        ["09100", "Support activities for petroleum and natural gas mining"],
        ["09900", "Support activities for other mining and quarrying"],
    ]
  C = [
    ["10110", "Processing and preserving of meat"],
    ["10120", "Processing and preserving of poultry meat"],
    ["10130", "Production of meat and poultry meat products"],
    ["10200", "Processing and preserving of fish, crustaceans and molluscs"],
    ["10310", "Processing and preserving of potatoes"],
    ["10320", "Manufacture of fruit and vegetable juice"],
    ["10390", "Other processing and preserving of fruit and vegetables"],
    ["10410", "Manufacture of oils and fats"],
    ["10420", "Manufacture of margarine and similar edible fats"],
    ["10511", "Liquid milk and cream production"],
    ["10512", "Butter and cheese production"],
    ["10519", "Manufacture of other milk products"],
    ["10520", "Manufacture of ice cream"],
    ["10611", "Grain milling"],
    ["10612", "Manufacture of breakfast cereals and cereals-based food"],
    ["10620", "Manufacture of starches and starch products"],
    ["10710", "Manufacture of bread; manufacture of fresh pastry goods and cakes"],
    ["10720", "Manufacture of rusks and biscuits; manufacture of preserved pastry goods and cakes"],
    ["10730", "Manufacture of macaroni, noodles, couscous and similar farinaceous products"],
    ["10810", "Manufacture of sugar"],
    ["10821", "Manufacture of cocoa and chocolate confectionery"],
    ["10822", "Manufacture of sugar confectionery"],
    ["10831", "Tea processing"],
    ["10832", "Production of coffee and coffee substitutes"],
    ["10840", "Manufacture of condiments and seasonings"],
    ["10850", "Manufacture of prepared meals and dishes"],
    ["10860", "Manufacture of homogenized food preparations and dietetic food"],
    ["10890", "Manufacture of other food products n.e.c."],
    ["10910", "Manufacture of prepared feeds for farm animals"],
    ["10920", "Manufacture of prepared pet foods"],
    ["11010", "Distilling, rectifying and blending of spirits"],
    ["11020", "Manufacture of wine from grape"],
    ["11030", "Manufacture of cider and other fruit wines"],
    ["11040", "Manufacture of other non-distilled fermented beverages"],
    ["11050", "Manufacture of beer"],
    ["11060", "Manufacture of malt"],
    ["11070", "Manufacture of soft drinks; production of mineral waters and other bottled waters"],
    ["12000", "Manufacture of tobacco products"],
    ["13100", "Preparation and spinning of textile fibres"],
    ["13200", "Weaving of textiles"],
    ["13300", "Finishing of textiles"],
    ["13910", "Manufacture of knitted and crocheted fabrics"],
    ["13921", "Manufacture of soft furnishings"],
    ["13922", "Manufacture of canvas goods, sacks, etc."],
    ["13923", "Manufacture of household textiles"],
    ["13931", "Manufacture of woven or tufted carpets and rugs"],
    ["13939", "Manufacture of other carpets and rugs"],
    ["13940", "Manufacture of cordage, rope, twine and netting"],
    ["13950", "Manufacture of non-wovens and articles made from non-wovens, except apparel"],
    ["13960", "Manufacture of other technical and industrial textiles"],
    ["13990", "Manufacture of other textiles n.e.c."],
    ["14110", "Manufacture of leather clothes"],
    ["14120", "Manufacture of workwear"],
    ["14131", "Manufacture of other men's outerwear"],
    ["14132", "Manufacture of other women's outerwear"],
    ["14141", "Manufacture of men's underwear"],
    ["14142", "Manufacture of women's underwear"],
    ["14190", "Manufacture of other wearing apparel and accessories n.e.c."],
    ["14200", "Manufacture of articles of fur"],
    ["14310", "Manufacture of knitted and crocheted hosiery"],
    ["14390", "Manufacture of other knitted and crocheted apparel"],
    ["15110", "Tanning and dressing of leather; dressing and dyeing of fur"],
    ["15120", "Manufacture of luggage, handbags and the like, saddlery and harness"],
    ["15200", "Manufacture of footwear"],
    ["16100", "Sawmilling and planing of wood"],
    ["16210", "Manufacture of veneer sheets and wood-based panels"],
    ["16220", "Manufacture of assembled parquet floors"],
    ["16230", "Manufacture of other builders' carpentry and joinery"],
    ["16240", "Manufacture of wooden containers"],
    ["16290", "Manufacture of other products of wood; manufacture of articles of cork, straw and plaiting materials"],
    ["17110", "Manufacture of pulp"],
    ["17120", "Manufacture of paper and paperboard"],
    ["17211", "Manufacture of corrugated paper and paperboard, sacks and bags"],
    ["17219", "Manufacture of other paper and paperboard containers"],
    ["17220", "Manufacture of household and sanitary goods and of toilet requisites"],
    ["17230", "Manufacture of paper stationery"],
    ["17240", "Manufacture of wallpaper"],
    ["17290", "Manufacture of other articles of paper and paperboard n.e.c."],
    ["18110", "Printing of newspapers"],
    ["18121", "Manufacture of printed labels"],
    ["18129", "Printing n.e.c."],
    ["18130", "Pre-press and pre-media services"],
    ["18140", "Binding and related services"],
    ["18201", "Reproduction of sound recording"],
    ["18202", "Reproduction of video recording"],
    ["18203", "Reproduction of computer media"],
    ["19100", "Manufacture of coke oven products"],
    ["19201", "Mineral oil refining"],
    ["19209", "Other treatment of petroleum products (excluding petrochemicals manufacture)"],
    ["20110", "Manufacture of industrial gases"],
    ["20120", "Manufacture of dyes and pigments"],
    ["20130", "Manufacture of other inorganic basic chemicals"],
    ["20140", "Manufacture of other organic basic chemicals"],
    ["20150", "Manufacture of fertilizers and nitrogen compounds"],
    ["20160", "Manufacture of plastics in primary forms"],
    ["20170", "Manufacture of synthetic rubber in primary forms"],
    ["20200", "Manufacture of pesticides and other agrochemical products"],
    ["20301", "Manufacture of paints, varnishes and similar coatings, mastics and sealants"],
    ["20302", "Manufacture of printing ink"],
    ["20411", "Manufacture of soap and detergents"],
    ["20412", "Manufacture of cleaning and polishing preparations"],
    ["20420", "Manufacture of perfumes and toilet preparations"],
    ["20510", "Manufacture of explosives"],
    ["20520", "Manufacture of glues"],
    ["20530", "Manufacture of essential oils"],
    ["20590", "Manufacture of other chemical products n.e.c."],
    ["20600", "Manufacture of man-made fibres"],
    ["21100", "Manufacture of basic pharmaceutical products"],
    ["21200", "Manufacture of pharmaceutical preparations"],
    ["22110", "Manufacture of rubber tyres and tubes; retreading and rebuilding of rubber tyres"],
    ["22190", "Manufacture of other rubber products"],
    ["22210", "Manufacture of plastic plates, sheets, tubes and profiles"],
    ["22220", "Manufacture of plastic packing goods"],
    ["22230", "Manufacture of builders ware of plastic"],
    ["22290", "Manufacture of other plastic products"],
    ["23110", "Manufacture of flat glass"],
    ["23120", "Shaping and processing of flat glass"],
    ["23130", "Manufacture of hollow glass"],
    ["23140", "Manufacture of glass fibres"],
    ["23190", "Manufacture and processing of other glass, including technical glassware"],
    ["23200", "Manufacture of refractory products"],
    ["23310", "Manufacture of ceramic tiles and flags"],
    ["23320", "Manufacture of bricks, tiles and construction products, in baked clay"],
    ["23410", "Manufacture of ceramic household and ornamental articles"],
    ["23420", "Manufacture of ceramic sanitary fixtures"],
    ["23430", "Manufacture of ceramic insulators and insulating fittings"],
    ["23440", "Manufacture of other technical ceramic products"],
    ["23490", "Manufacture of other ceramic products n.e.c."],
    ["23510", "Manufacture of cement"],
    ["23520", "Manufacture of lime and plaster"],
    ["23610", "Manufacture of concrete products for construction purposes"],
    ["23620", "Manufacture of plaster products for construction purposes"],
    ["23630", "Manufacture of ready-mixed concrete"],
    ["23640", "Manufacture of mortars"],
    ["23650", "Manufacture of fibre cement"],
    ["23690", "Manufacture of other articles of concrete, plaster and cement"],
    ["23700", "Cutting, shaping and finishing of stone"],
    ["23910", "Production of abrasive products"],
    ["23990", "Manufacture of other non-metallic mineral products n.e.c."],
    ["24100", "Manufacture of basic iron and steel and of ferro-alloys"],
    ["24200", "Manufacture of tubes, pipes, hollow profiles and related fittings, of steel"],
    ["24310", "Cold drawing of bars"],
    ["24320", "Cold rolling of narrow strip"],
    ["24330", "Cold forming or folding"],
    ["24340", "Cold drawing of wire"],
    ["24410", "Precious metals production"],
    ["24420", "Aluminium production"],
    ["24430", "Lead, zinc and tin production"],
    ["24440", "Copper production"],
    ["24450", "Other non-ferrous metal production"],
    ["24460", "Processing of nuclear fuel"],
    ["24510", "Casting of iron"],
    ["24520", "Casting of steel"],
    ["24530", "Casting of light metals"],
    ["24540", "Casting of other non-ferrous metals"],
    ["25110", "Manufacture of metal structures and parts of structures"],
    ["25120", "Manufacture of doors and windows of metal"],
    ["25210", "Manufacture of central heating radiators and boilers"],
    ["25290", "Manufacture of other tanks, reservoirs and containers of metal"],
    ["25300", "Manufacture of steam generators, except central heating hot water boilers"],
    ["25400", "Manufacture of weapons and ammunition"],
    ["25500", "Forging, pressing, stamping and roll-forming of metal; powder metallurgy"],
    ["25610", "Treatment and coating of metals"],
    ["25620", "Machining"],
    ["25710", "Manufacture of cutlery"],
    ["25720", "Manufacture of locks and hinges"],
    ["25730", "Manufacture of tools"],
    ["25910", "Manufacture of steel drums and similar containers"],
    ["25920", "Manufacture of light metal packaging"],
    ["25930", "Manufacture of wire products, chain and springs"],
    ["25940", "Manufacture of fasteners and screw machine products"],
    ["25990", "Manufacture of other fabricated metal products n.e.c."],
    ["26110", "Manufacture of electronic components"],
    ["26120", "Manufacture of loaded electronic boards"],
    ["26200", "Manufacture of computers and peripheral equipment"],
    ["26301", "Manufacture of telegraph and telephone apparatus and equipment"],
    ["26309", "Manufacture of communication equipment other than telegraph, and telephone apparatus and equipment"],
    ["26400", "Manufacture of consumer electronics"],
    ["26511", "Manufacture of electronic measuring, testing etc. equipment, not for industrial process control"],
    ["26512", "Manufacture of electronic industrial process control equipment"],
    ["26513", "Manufacture of non-electronic measuring, testing etc. equipment, not for industrial process control"],
    ["26514", "Manufacture of non-electronic industrial process control equipment"],
    ["26520", "Manufacture of watches and clocks"],
    ["26600", "Manufacture of irradiation, electromedical and electrotherapeutic equipment"],
    ["26701", "Manufacture of optical precision instruments"],
    ["26702", "Manufacture of photographic and cinematographic equipment"],
    ["26800", "Manufacture of magnetic and optical media"],
    ["27110", "Manufacture of electric motors, generators and transformers"],
    ["27120", "Manufacture of electricity distribution and control apparatus"],
    ["27200", "Manufacture of batteries and accumulators"],
    ["27310", "Manufacture of fibre optic cables"],
    ["27320", "Manufacture of other electronic and electric wires and cables"],
    ["27330", "Manufacture of wiring devices"],
    ["27400", "Manufacture of electric lighting equipment"],
    ["27510", "Manufacture of electric domestic appliances"],
    ["27520", "Manufacture of non-electric domestic appliances"],
    ["27900", "Manufacture of other electrical equipment"],
    ["28110", "Manufacture of engines and turbines, except aircraft, vehicle and cycle engines"],
    ["28120", "Manufacture of fluid power equipment"],
    ["28131", "Manufacture of pumps"],
    ["28132", "Manufacture of compressors"],
    ["28140", "Manufacture of taps and valves"],
    ["28150", "Manufacture of bearings, gears, gearing and driving elements"],
    ["28210", "Manufacture of ovens, furnaces and furnace burners"],
    ["28220", "Manufacture of lifting and handling equipment"],
    ["28230", "Manufacture of office machinery and equipment (except computers and peripheral equipment)"],
    ["28240", "Manufacture of power-driven hand tools"],
    ["28250", "Manufacture of non-domestic cooling and ventilation equipment"],
    ["28290", "Manufacture of other general-purpose machinery n.e.c."],
    ["28301", "Manufacture of agricultural tractors"],
    ["28302", "Manufacture of agricultural and forestry machinery other than tractors"],
    ["28410", "Manufacture of metal forming machinery"],
    ["28490", "Manufacture of other machine tools"],
    ["28910", "Manufacture of machinery for metallurgy"],
    ["28921", "Manufacture of machinery for mining"],
    ["28922", "Manufacture of earthmoving equipment"],
    ["28923", "Manufacture of equipment for concrete crushing and screening and roadworks"],
    ["28930", "Manufacture of machinery for food, beverage and tobacco processing"],
    ["28940", "Manufacture of machinery for textile, apparel and leather production"],
    ["28950", "Manufacture of machinery for paper and paperboard production"],
    ["28960", "Manufacture of plastics and rubber machinery"],
    ["28990", "Manufacture of other special-purpose machinery n.e.c."],
    ["29100", "Manufacture of motor vehicles"],
    ["29201", "Manufacture of bodies (coachwork) for motor vehicles (except caravans)"],
    ["29202", "Manufacture of trailers and semi-trailers"],
    ["29203", "Manufacture of caravans"],
    ["29310", "Manufacture of electrical and electronic equipment for motor vehicles and their engines"],
    ["29320", "Manufacture of other parts and accessories for motor vehicles"],
    ["30110", "Building of ships and floating structures"],
    ["30120", "Building of pleasure and sporting boats"],
    ["30200", "Manufacture of railway locomotives and rolling stock"],
    ["30300", "Manufacture of air and spacecraft and related machinery"],
    ["30400", "Manufacture of military fighting vehicles"],
    ["30910", "Manufacture of motorcycles"],
    ["30920", "Manufacture of bicycles and invalid carriages"],
    ["30990", "Manufacture of other transport equipment n.e.c."],
    ["31010", "Manufacture of office and shop furniture"],
    ["31020", "Manufacture of kitchen furniture"],
    ["31030", "Manufacture of mattresses"],
    ["31090", "Manufacture of other furniture"],
    ["32110", "Striking of coins"],
    ["32120", "Manufacture of jewellery and related articles"],
    ["32130", "Manufacture of imitation jewellery and related articles"],
    ["32200", "Manufacture of musical instruments"],
    ["32300", "Manufacture of sports goods"],
    ["32401", "Manufacture of professional and arcade games and toys"],
    ["32409", "Manufacture of other games and toys, n.e.c."],
    ["32500", "Manufacture of medical and dental instruments and supplies"],
    ["32910", "Manufacture of brooms and brushes"],
    ["32990", "Other manufacturing n.e.c."],
    ["33110", "Repair of fabricated metal products"],
    ["33120", "Repair of machinery"],
    ["33130", "Repair of electronic and optical equipment"],
    ["33140", "Repair of electrical equipment"],
    ["33150", "Repair and maintenance of ships and boats"],
    ["33160", "Repair and maintenance of aircraft and spacecraft"],
    ["33170", "Repair and maintenance of other transport equipment n.e.c."],
    ["33190", "Repair of other equipment"],
    ["33200", "Installation of industrial machinery and equipment"]
]
  D = [
        ["35110", "Production of electricity"],
        ["35120", "Transmission of electricity"],
        ["35130", "Distribution of electricity"],
        ["35140", "Trade of electricity"],
        ["35210", "Manufacture of gas"],
        ["35220", "Distribution of gaseous fuels through mains"],
        ["35230", "Trade of gas through mains"],
        ["35300", "Steam and air conditioning supply"],
    ]
  E = [
        ["36000", "Water collection, treatment and supply"],
        ["37000", "Sewerage"],
        ["38110", "Collection of non-hazardous waste"],
        ["38120", "Collection of hazardous waste"],
        ["38210", "Treatment and disposal of non-hazardous waste"],
        ["38220", "Treatment and disposal of hazardous waste"],
        ["38310", "Dismantling of wrecks"],
        ["38320", "Recovery of sorted materials"],
        ["39000", "Remediation activities and other waste management services"],
    ]
  F = [
        ["41100", "Development of building projects"],
        ["41201", "Construction of commercial buildings"],
        ["41202", "Construction of domestic buildings"],
        ["42110", "Construction of roads and motorways"],
        ["42120", "Construction of railways and underground railways"],
        ["42130", "Construction of bridges and tunnels"],
        ["42210", "Construction of utility projects for fluids"],
        ["42220", "Construction of utility projects for electricity and telecommunications"],
        ["42910", "Construction of water projects"],
        ["42990", "Construction of other civil engineering projects n.e.c."],
        ["43110", "Demolition"],
        ["43120", "Site preparation"],
        ["43130", "Test drilling and boring"],
        ["43210", "Electrical installation"],
        ["43220", "Plumbing, heat and air-conditioning installation"],
        ["43290", "Other construction installation"],
        ["43310", "Plastering"],
        ["43320", "Joinery installation"],
        ["43330", "Floor and wall covering"],
        ["43341", "Painting"],
        ["43342", "Glazing"],
        ["43390", "Other building completion and finishing"],
        ["43910", "Roofing activities"],
        ["43991", "Scaffold erection"],
        ["43999", "Other specialised construction activities n.e.c."],
    ]
  G = [
    ["45111", "Sale of new cars and light motor vehicles"],
    ["45112", "Sale of used cars and light motor vehicles"],
    ["45190", "Sale of other motor vehicles"],
    ["45200", "Maintenance and repair of motor vehicles"],
    ["45310", "Wholesale trade of motor vehicle parts and accessories"],
    ["45320", "Retail trade of motor vehicle parts and accessories"],
    ["45400", "Sale, maintenance and repair of motorcycles and related parts and accessories"],
    ["46110", "Agents selling agricultural raw materials, livestock, textile raw materials and semi-finished goods"],
    ["46120", "Agents involved in the sale of fuels, ores, metals and industrial chemicals"],
    ["46130", "Agents involved in the sale of timber and building materials"],
    ["46140", "Agents involved in the sale of machinery, industrial equipment, ships and aircraft"],
    ["46150", "Agents involved in the sale of furniture, household goods, hardware and ironmongery"],
    ["46160", "Agents involved in the sale of textiles, clothing, fur, footwear and leather goods"],
    ["46170", "Agents involved in the sale of food, beverages and tobacco"],
    ["46180", "Agents specialised in the sale of other particular products"],
    ["46190", "Agents involved in the sale of a variety of goods"],
    ["46210", "Wholesale of grain, unmanufactured tobacco, seeds and animal feeds"],
    ["46220", "Wholesale of flowers and plants"],
    ["46230", "Wholesale of live animals"],
    ["46240", "Wholesale of hides, skins and leather"],
    ["46310", "Wholesale of fruit and vegetables"],
    ["46320", "Wholesale of meat and meat products"],
    ["46330", "Wholesale of dairy products, eggs and edible oils and fats"],
    ["46341", "Wholesale of fruit and vegetable juices, mineral water and soft drinks"],
    ["46342", "Wholesale of wine, beer, spirits and other alcoholic beverages"],
    ["46350", "Wholesale of tobacco products"],
    ["46360", "Wholesale of sugar and chocolate and sugar confectionery"],
    ["46370", "Wholesale of coffee, tea, cocoa and spices"],
    ["46380", "Wholesale of other food, including fish, crustaceans and molluscs"],
    ["46390", "Non-specialised wholesale of food, beverages and tobacco"],
    ["46410", "Wholesale of textiles"],
    ["46420", "Wholesale of clothing and footwear"],
    ["46431", "Wholesale of audio tapes, records, CDs and video tapes and the equipment on which these are played"],
    ["46439", "Wholesale of radio, television goods & electrical household appliances (other than records, tapes, CD's & video tapes and the equipment used for playing them)"],
    ["46440", "Wholesale of china and glassware and cleaning materials"],
    ["46450", "Wholesale of perfume and cosmetics"],
    ["46460", "Wholesale of pharmaceutical goods"],
    ["46470", "Wholesale of furniture, carpets and lighting equipment"],
    ["46480", "Wholesale of watches and jewellery"],
    ["46491", "Wholesale of musical instruments"],
    ["46499", "Wholesale of household goods (other than musical instruments) n.e.c"],
    ["46510", "Wholesale of computers, computer peripheral equipment and software"],
    ["46520", "Wholesale of electronic and telecommunications equipment and parts"],
    ["46610", "Wholesale of agricultural machinery, equipment and supplies"],
    ["46620", "Wholesale of machine tools"],
    ["46630", "Wholesale of mining, construction and civil engineering machinery"],
    ["46640", "Wholesale of machinery for the textile industry and of sewing and knitting machines"],
    ["46650", "Wholesale of office furniture"],
    ["46660", "Wholesale of other office machinery and equipment"],
    ["46690", "Wholesale of other machinery and equipment"],
    ["46711", "Wholesale of petroleum and petroleum products"],
    ["46719", "Wholesale of other fuels and related products"],
    ["46720", "Wholesale of metals and metal ores"],
    ["46730", "Wholesale of wood, construction materials and sanitary equipment"],
    ["46740", "Wholesale of hardware, plumbing and heating equipment and supplies"],
    ["46750", "Wholesale of chemical products"],
    ["46760", "Wholesale of other intermediate products"],
    ["46770", "Wholesale of waste and scrap"],
    ["46900", "Non-specialised wholesale trade"],
    ["47110", "Retail sale in non-specialised stores with food, beverages or tobacco predominating"],
    ["47190", "Other retail sale in non-specialised stores"],
    ["47210", "Retail sale of fruit and vegetables in specialised stores"],
    ["47220", "Retail sale of meat and meat products in specialised stores"],
    ["47230", "Retail sale of fish, crustaceans and molluscs in specialised stores"],
    ["47240", "Retail sale of bread, cakes, flour confectionery and sugar confectionery in specialised stores"],
    ["47250", "Retail sale of beverages in specialised stores"],
    ["47260", "Retail sale of tobacco products in specialised stores"],
    ["47290", "Other retail sale of food in specialised stores"],
    ["47300", "Retail sale of automotive fuel in specialised stores"],
    ["47410", "Retail sale of computers, peripheral units and software in specialised stores"],
    ["47421", "Retail sale of mobile telephones"],
    ["47429", "Retail sale of telecommunications equipment other than mobile telephones"],
    ["47430", "Retail sale of audio and video equipment in specialised stores"],
    ["47510", "Retail sale of textiles in specialised stores"],
    ["47520", "Retail sale of hardware, paints and glass in specialised stores"],
    ["47530", "Retail sale of carpets, rugs, wall and floor coverings in specialised stores"],
    ["47540", "Retail sale of electrical household appliances in specialised stores"],
    ["47591", "Retail sale of musical instruments and scores"],
    ["47599", "Retail of furniture, lighting, and similar (not musical instruments or scores) in specialised store"],
    ["47610", "Retail sale of books in specialised stores"],
    ["47620", "Retail sale of newspapers and stationery in specialised stores"],
    ["47630", "Retail sale of music and video recordings in specialised stores"],
    ["47640", "Retail sale of sports goods, fishing gear, camping goods, boats and bicycles"],
    ["47650", "Retail sale of games and toys in specialised stores"],
    ["47710", "Retail sale of clothing in specialised stores"],
    ["47721", "Retail sale of footwear in specialised stores"],
    ["47722", "Retail sale of leather goods in specialised stores"],
    ["47730", "Dispensing chemist in specialised stores"],
    ["47741", "Retail sale of hearing aids"],
    ["47749", "Retail sale of medical and orthopaedic goods in specialised stores (not incl. hearing aids) n.e.c."],
    ["47750", "Retail sale of cosmetic and toilet articles in specialised stores"],
    ["47760", "Retail sale of flowers, plants, seeds, fertilizers, pet animals and pet food in specialised stores"],
    ["47770", "Retail sale of watches and jewellery in specialised stores"],
    ["47781", "Retail sale in commercial art galleries"],
    ["47782", "Retail sale by opticians"],
    ["47789", "Other retail sale of new goods in specialised stores (not commercial art galleries and opticians)"],
    ["47791", "Retail sale of antiques including antique books in stores"],
    ["47799", "Retail sale of other second-hand goods in stores (not incl. antiques)"],
    ["47810", "Retail sale via stalls and markets of food, beverages and tobacco products"],
    ["47820", "Retail sale via stalls and markets of textiles, clothing and footwear"],
    ["47890", "Retail sale via stalls and markets of other goods"],
    ["47910", "Retail sale via mail order houses or via Internet"],
    ["47990", "Other retail sale not in stores, stalls or markets"]
]
  H = [
        ["49100", "Passenger rail transport, interurban"],
        ["49200", "Freight rail transport"],
        ["49311", "Urban and suburban passenger railway transportation by underground, metro and similar systems"],
        ["49319", "Other urban, suburban or metropolitan passenger land transport (not underground, metro or similar)"],
        ["49320", "Taxi operation"],
        ["49390", "Other passenger land transport"],
        ["49410", "Freight transport by road"],
        ["49420", "Removal services"],
        ["49500", "Transport via pipeline"],
        ["50100", "Sea and coastal passenger water transport"],
        ["50200", "Sea and coastal freight water transport"],
        ["50300", "Inland passenger water transport"],
        ["50400", "Inland freight water transport"],
        ["51101", "Scheduled passenger air transport"],
        ["51102", "Non-scheduled passenger air transport"],
        ["51210", "Freight air transport"],
        ["51220", "Space transport"],
        ["52101", "Operation of warehousing and storage facilities for water transport activities"],
        ["52102", "Operation of warehousing and storage facilities for air transport activities"],
        ["52103", "Operation of warehousing and storage facilities for land transport activities"],
        ["52211", "Operation of rail freight terminals"],
        ["52212", "Operation of rail passenger facilities at railway stations"],
        ["52213", "Operation of bus and coach passenger facilities at bus and coach stations"],
        ["52219", "Other service activities incidental to land transportation, n.e.c."],
        ["52220", "Service activities incidental to water transportation"],
        ["52230", "Service activities incidental to air transportation"],
        ["52241", "Cargo handling for water transport activities"],
        ["52242", "Cargo handling for air transport activities"],
        ["52243", "Cargo handling for land transport activities"],
        ["52290", "Other transportation support activities"],
        ["53100", "Postal activities under universal service obligation"],
        ["53201", "Licensed carriers"],
        ["53202", "Unlicensed carriers"],
    ]
  I = [
        ["55100", "Hotels and similar accommodation"],
        ["55201", "Holiday centres and villages"],
        ["55202", "Youth hostels"],
        ["55209", "Other holiday and other collective accommodation"],
        ["55300", "Recreational vehicle parks, trailer parks and camping grounds"],
        ["55900", "Other accommodation"],
        ["56101", "Licenced restaurants"],
        ["56102", "Unlicenced restaurants and cafes"],
        ["56103", "Take-away food shops and mobile food stands"],
        ["56210", "Event catering activities"],
        ["56290", "Other food services"],
        ["56301", "Licenced clubs"],
        ["56302", "Public houses and bars"],
    ]
  J = [
        ["58110", "Book publishing"],
        ["58120", "Publishing of directories and mailing lists"],
        ["58130", "Publishing of newspapers"],
        ["58141", "Publishing of learned journals"],
        ["58142", "Publishing of consumer and business journals and periodicals"],
        ["58190", "Other publishing activities"],
        ["58210", "Publishing of computer games"],
        ["58290", "Other software publishing"],
        ["59111", "Motion picture production activities"],
        ["59112", "Video production activities"],
        ["59113", "Television programme production activities"],
        ["59120", "Motion picture, video and television programme post-production activities"],
        ["59131", "Motion picture distribution activities"],
        ["59132", "Video distribution activities"],
        ["59133", "Television programme distribution activities"],
        ["59140", "Motion picture projection activities"],
        ["59200", "Sound recording and music publishing activities"],
        ["60100", "Radio broadcasting"],
        ["60200", "Television programming and broadcasting activities"],
        ["61100", "Wired telecommunications activities"],
        ["61200", "Wireless telecommunications activities"],
        ["61300", "Satellite telecommunications activities"],
        ["61900", "Other telecommunications activities"],
        ["62011", "Ready-made interactive leisure and entertainment software development"],
        ["62012", "Business and domestic software development"],
        ["62020", "Information technology consultancy activities"],
        ["62030", "Computer facilities management activities"],
        ["62090", "Other information technology service activities"],
        ["63110", "Data processing, hosting and related activities"],
        ["63120", "Web portals"],
        ["63910", "News agency activities"],
        ["63990", "Other information service activities n.e.c."],
    ]
  K = [
    ["64110", "Central banking"],
    ["64191", "Banks"],
    ["64192", "Building societies"],
    ["64201", "Activities of agricultural holding companies"],
    ["64202", "Activities of production holding companies"],
    ["64203", "Activities of construction holding companies"],
    ["64204", "Activities of distribution holding companies"],
    ["64205", "Activities of financial services holding companies"],
    ["64209", "Activities of other holding companies n.e.c."],
    ["64301", "Activities of investment trusts"],
    ["64302", "Activities of unit trusts"],
    ["64303", "Activities of venture and development capital companies"],
    ["64304", "Activities of open-ended investment companies"],
    ["64305", "Activities of property unit trusts"],
    ["64306", "Activities of real estate investment trusts"],
    ["64910", "Financial leasing"],
    ["64921", "Credit granting by non-deposit taking finance houses and other specialist consumer credit grantors"],
    ["64922", "Activities of mortgage finance companies"],
    ["64929", "Other credit granting n.e.c."],
    ["64991", "Security dealing on own account"],
    ["64992", "Factoring"],
    ["64999", "Financial intermediation not elsewhere classified"],
    ["65110", "Life insurance"],
    ["65120", "Non-life insurance"],
    ["65201", "Life reinsurance"],
    ["65202", "Non-life reinsurance"],
    ["65300", "Pension funding"],
    ["66110", "Administration of financial markets"],
    ["66120", "Security and commodity contracts dealing activities"],
    ["66190", "Activities auxiliary to financial intermediation n.e.c."],
    ["66210", "Risk and damage evaluation"],
    ["66220", "Activities of insurance agents and brokers"],
    ["66290", "Other activities auxiliary to insurance and pension funding"],
    ["66300", "Fund management activities"]
]
  L = [
        ["68100", "Buying and selling of own real estate"],
        ["68201", "Renting and operating of Housing Association real estate"],
        ["68202", "Letting and operating of conference and exhibition centres"],
        ["68209", "Other letting and operating of own or leased real estate"],
        ["68310", "Real estate agencies"],
        ["68320", "Management of real estate on a fee or contract basis"],
    ]
  M = [
        ["69101", "Barristers at law"],
        ["69102", "Solicitors"],
        ["69109", "Activities of patent and copyright agents; other legal activities n.e.c."],
        ["69201", "Accounting and auditing activities"],
        ["69202", "Bookkeeping activities"],
        ["69203", "Tax consultancy"],
        ["70100", "Activities of head offices"],
        ["70210", "Public relations and communications activities"],
        ["70221", "Financial management"],
        ["70229", "Management consultancy activities other than financial management"],
        ["71111", "Architectural activities"],
        ["71112", "Urban planning and landscape architectural activities"],
        ["71121", "Engineering design activities for industrial process and production"],
        ["71122", "Engineering related scientific and technical consulting activities"],
        ["71129", "Other engineering activities"],
        ["71200", "Technical testing and analysis"],
        ["72110", "Research and experimental development on biotechnology"],
        ["72190", "Other research and experimental development on natural sciences and engineering"],
        ["72200", "Research and experimental development on social sciences and humanities"],
        ["73110", "Advertising agencies"],
        ["73120", "Media representation services"],
        ["73200", "Market research and public opinion polling"],
        ["74100", "Specialised design activities"],
        ["74201", "Portrait photographic activities"],
        ["74202", "Other specialist photography"],
        ["74203", "Film processing"],
        ["74209", "Photographic activities not elsewhere classified"],
        ["74300", "Translation and interpretation activities"],
        ["74901", "Environmental consulting activities"],
        ["74902", "Quantity surveying activities"],
        ["74909", "Other professional, scientific and technical activities n.e.c."],
        ["74990", "Non-trading company"],
        ["75000", "Veterinary activities"],
    ]
  N = [
    ["77110", "Renting and leasing of cars and light motor vehicles"],
    ["77120", "Renting and leasing of trucks and other heavy vehicles"],
    ["77210", "Renting and leasing of recreational and sports goods"],
    ["77220", "Renting of video tapes and disks"],
    ["77291", "Renting and leasing of media entertainment equipment"],
    ["77299", "Renting and leasing of other personal and household goods"],
    ["77310", "Renting and leasing of agricultural machinery and equipment"],
    ["77320", "Renting and leasing of construction and civil engineering machinery and equipment"],
    ["77330", "Renting and leasing of office machinery and equipment (including computers)"],
    ["77341", "Renting and leasing of passenger water transport equipment"],
    ["77342", "Renting and leasing of freight water transport equipment"],
    ["77351", "Renting and leasing of air passenger transport equipment"],
    ["77352", "Renting and leasing of freight air transport equipment"],
    ["77390", "Renting and leasing of other machinery, equipment and tangible goods n.e.c."],
    ["77400", "Leasing of intellectual property and similar products, except copyright works"],
    ["78101", "Motion picture, television and other theatrical casting activities"],
    ["78109", "Other activities of employment placement agencies"],
    ["78200", "Temporary employment agency activities"],
    ["78300", "Human resources provision and management of human resources functions"],
    ["79110", "Travel agency activities"],
    ["79120", "Tour operator activities"],
    ["79901", "Activities of tourist guides"],
    ["79909", "Other reservation service activities n.e.c."],
    ["80100", "Private security activities"],
    ["80200", "Security systems service activities"],
    ["80300", "Investigation activities"],
    ["81100", "Combined facilities support activities"],
    ["81210", "General cleaning of buildings"],
    ["81221", "Window cleaning services"],
    ["81222", "Specialised cleaning services"],
    ["81223", "Furnace and chimney cleaning services"],
    ["81229", "Other building and industrial cleaning activities"],
    ["81291", "Disinfecting and exterminating services"],
    ["81299", "Other cleaning services"],
    ["81300", "Landscape service activities"],
    ["82110", "Combined office administrative service activities"],
    ["82190", "Photocopying, document preparation and other specialised office support activities"],
    ["82200", "Activities of call centres"],
    ["82301", "Activities of exhibition and fair organisers"],
    ["82302", "Activities of conference organisers"],
    ["82911", "Activities of collection agencies"],
    ["82912", "Activities of credit bureaus"],
    ["82920", "Packaging activities"],
    ["82990", "Other business support service activities n.e.c."]
]
  O = [
        ["84110", "General public administration activities"],
        ["84120", "Regulation of health care, education, cultural and other social services, not incl. social security"],
        ["84130", "Regulation of and contribution to more efficient operation of businesses"],
        ["84210", "Foreign affairs"],
        ["84220", "Defence activities"],
        ["84230", "Justice and judicial activities"],
        ["84240", "Public order and safety activities"],
        ["84250", "Fire service activities"],
        ["84300", "Compulsory social security activities"],
    ]
  P = [
        ["85100", "Pre-primary education"],
        ["85200", "Primary education"],
        ["85310", "General secondary education"],
        ["85320", "Technical and vocational secondary education"],
        ["85410", "Post-secondary non-tertiary education"],
        ["85421", "First-degree level higher education"],
        ["85422", "Post-graduate level higher education"],
        ["85510", "Sports and recreation education"],
        ["85520", "Cultural education"],
        ["85530", "Driving school activities"],
        ["85590", "Other education n.e.c."],
        ["85600", "Educational support services"],
    ]
  Q = [
    ["86101", "Hospital activities"],
    ["86102", "Medical nursing home activities"],
    ["86210", "General medical practice activities"],
    ["86220", "Specialists medical practice activities"],
    ["86230", "Dental practice activities"],
    ["86900", "Other human health activities"],
    ["87100", "Residential nursing care facilities"],
    ["87200", "Residential care activities for learning difficulties, mental health and substance abuse"],
    ["87300", "Residential care activities for the elderly and disabled"],
    ["87900", "Other residential care activities n.e.c."],
    ["88100", "Social work activities without accommodation for the elderly and disabled"],
    ["88910", "Child day-care activities"],
    ["88990", "Other social work activities without accommodation n.e.c."]
]
  R = [
        ["90010", "Performing arts"],
        ["90020", "Support activities to performing arts"],
        ["90030", "Artistic creation"],
        ["90040", "Operation of arts facilities"],
        ["91011", "Library activities"],
        ["91012", "Archives activities"],
        ["91020", "Museums activities"],
        ["91030", "Operation of historical sites and buildings and similar visitor attractions"],
        ["91040", "Botanical and zoological gardens and nature reserves activities"],
        ["92000", "Gambling and betting activities"],
        ["93110", "Operation of sports facilities"],
        ["93120", "Activities of sport clubs"],
        ["93130", "Fitness facilities"],
        ["93191", "Activities of racehorse owners"],
        ["93199", "Other sports activities"],
        ["93210", "Activities of amusement parks and theme parks"],
        ["93290", "Other amusement and recreation activities n.e.c."],
    ]
  S = [
        ["94110", "Activities of business and employers membership organisations"],
        ["94120", "Activities of professional membership organisations"],
        ["94200", "Activities of trade unions"],
        ["94910", "Activities of religious organisations"],
        ["94920", "Activities of political organisations"],
        ["94990", "Activities of other membership organisations n.e.c."],
        ["95110", "Repair of computers and peripheral equipment"],
        ["95120", "Repair of communication equipment"],
        ["95210", "Repair of consumer electronics"],
        ["95220", "Repair of household appliances and home and garden equipment"],
        ["95230", "Repair of footwear and leather goods"],
        ["95240", "Repair of furniture and home furnishings"],
        ["95250", "Repair of watches, clocks and jewellery"],
        ["95290", "Repair of personal and household goods n.e.c."],
        ["96010", "Washing and (dry-)cleaning of textile and fur products"],
        ["96020", "Hairdressing and other beauty treatment"],
        ["96030", "Funeral and related activities"],
        ["96040", "Physical well-being activities"],
        ["96090", "Other service activities n.e.c."],
    ]
  T = [
        ["97000", "Activities of households as employers of domestic personnel"],
        ["98000", "Residents property management"],
        ["98100", "Undifferentiated goods-producing activities of private households for own use"],
        ["98200", "Undifferentiated service-producing activities of private households for own use"],
    ]
  U = [
        ["99000", "Activities of extraterritorial organisations and bodies"],
        ["99999", "Dormant Company"],
    ]
  
  try:
    # Assuming 'sectionResponse' contains the letter of the section identified by GPT
    selected_section = sectionResponse.strip().upper()

    #somehow deduce what section from the gpt response
    #dictionary of codes matching to letter
    section_codes = {
      "A": A,
      "B": B,
      "C": C,
      "D": D,
      "E": E,
      "F": F,
      "G": G,
      "H": H,
      "I": I,
      "J": J,
      "K": K,
      "L": L,
      "M": M,
      "N": N,
      "O": O,
      "P": P,
      "Q": Q,
      "R": R,
      "S": S,
      "T": T,
      "U": U,
        }
    #if the choice is in the section
    if selected_section in section_codes:
      selected_list = section_codes[selected_section]
      # Now you can use the selected_list as needed in your code
      print(selected_list)
    else:
      print("Invalid section identified")

  except:
     print("failed deducing section of sic code")    
  #
  
  #add all the possible sic codes of the section to the prompt
  promptLowLevelSelection="Based on the information you have recieved "+ allData+"Guess which of the following sic codes under the section you guessed this business falls under:"
  for code, description in selected_list:  # Iterate over elements directly
    str_to_add = code + " - " + description  # Access values directly
    promptLowLevelSelection += str_to_add

  promptLowLevelSelection+="Respond to this prompt only with one of the five digit sic code numbers(for example'94110'). If you cannot figure this out respond with the value of -1."
  codeResponse=aiProcess(promptLowLevelSelection)
  return codeResponse




#coicop codes---------------------------------------------------
def findNextCompany():
  #define a lsit of all of the high level catagories of coicop codes.
 
  #lists for each section of coicop
  section_1 = [
    {"Code": "01", "Description": "FOOD AND NON-ALCOHOLIC BEVERAGES",
     "Subcategories": [
        {"Code": "01.1", "Description": "FOOD",
         "Subcategories": [
            {"Code": "01.1.1", "Description": "Cereals and cereal products (ND)",
             "Subcategories": [
                {"Code": "01.1.1.1", "Description": "Cereals (ND)"},
                {"Code": "01.1.1.2", "Description": "Flour of cereals (ND)"},
                {"Code": "01.1.1.3", "Description": "Bread and bakery products (ND)"},
                {"Code": "01.1.1.4", "Description": "Breakfast cereals (ND)"},
                {"Code": "01.1.1.5", "Description": "Macaroni, noodles, couscous and similar pasta products (ND)"},
                {"Code": "01.1.1.9", "Description": "Other cereal and grain mill products (ND)"}
            ]},
            {"Code": "01.1.2", "Description": "Live animals, meat and other parts of slaughtered land animals (ND)",
             "Subcategories": [
                {"Code": "01.1.2.1", "Description": "Live land animals (ND)"},
                {"Code": "01.1.2.2", "Description": "Meat, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.2.3", "Description": "Meat, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.2.4", "Description": "Offal, blood and other parts of slaughtered animals, fresh, chilled or frozen, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.2.5", "Description": "Meat, offal, blood and other parts of slaughtered animals' preparations (ND)"}
            ]},
            {"Code": "01.1.3", "Description": "Fish and other seafood (ND)",
             "Subcategories": [
                {"Code": "01.1.3.1", "Description": "Fish, live, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.3.2", "Description": "Fish, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.3.3", "Description": "Fish preparations (ND)"},
                {"Code": "01.1.3.4", "Description": "Other seafood, live, fresh, chilled or frozen (ND)"},
                {"Code": "01.1.3.5", "Description": "Other seafood, dried, salted, in brine or smoked (ND)"},
                {"Code": "01.1.3.6", "Description": "Other seafood preparations (ND)"},
                {"Code": "01.1.3.7", "Description": "Livers, roes and offal of fish and of other seafood in all forms (ND)"}
            ]},
            {"Code": "01.1.4", "Description": "Milk, other dairy products and eggs (ND)",
             "Subcategories": [
                {"Code": "01.1.4.1", "Description": "Raw and whole milk (ND)"},
                {"Code": "01.1.4.2", "Description": "Skimmed milk (ND)"},
                {"Code": "01.1.4.3", "Description": "Other milk and cream (ND)"},
                {"Code": "01.1.4.4", "Description": "Non-animal milk (ND)"},
                {"Code": "01.1.4.5", "Description": "Cheese (ND)"},
                {"Code": "01.1.4.6", "Description": "Yoghurt and similar products (ND)"},
                {"Code": "01.1.4.7", "Description": "Milk-based dessert and beverages (ND)"},
                {"Code": "01.1.4.8", "Description": "Eggs (ND)"},
                {"Code": "01.1.4.9", "Description": "Other dairy products (ND)"}
            ]},
            {"Code": "01.1.5", "Description": "Oils and fats (ND)",
             "Subcategories": [
                {"Code": "01.1.5.1", "Description": "Vegetable oils (ND)"},
                {"Code": "01.1.5.2", "Description": "Butter and other fats and oils derived from milk (ND)"},
                {"Code": "01.1.5.3", "Description": "Margarine and similar preparations (ND)"},
                {"Code": "01.1.5.9", "Description": "Other animal oils and fats (ND)"}
            ]},
            {"Code": "01.1.6", "Description": "Fruits and nuts (ND)",
             "Subcategories": [
                {"Code": "01.1.6.1", "Description": "Dates, figs and tropical fruits, fresh (ND)"},
                {"Code": "01.1.6.2", "Description": "Citrus fruits, fresh (ND)"},
                {"Code": "01.1.6.3", "Description": "Stone fruits and pome fruits, fresh (ND)"},
                {"Code": "01.1.6.4", "Description": "Berries, fresh (ND)"},
                {"Code": "01.1.6.5", "Description": "Other fruits, fresh (ND)"},
                {"Code": "01.1.6.6", "Description": "Frozen fruit (ND)"},
                {"Code": "01.1.6.7", "Description": "Fruit, dried and dehydrated (ND)"},
                {"Code": "01.1.6.8", "Description": "Nuts, in shell or shelled (ND)"},
                {"Code": "01.1.6.9", "Description": "Fruit and nuts ground and other preparations (ND)"}
            ]},
            {"Code": "01.1.7", "Description": "Vegetables, tubers, plantains, cooking bananas and pulses (ND)",
             "Subcategories": [
                {"Code": "01.1.7.1", "Description": "Leafy or stem vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.2", "Description": "Fruit-bearing vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.3", "Description": "Green leguminous vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.4", "Description": "Other vegetables, fresh or chilled (ND)"},
                {"Code": "01.1.7.5", "Description": "Tubers, plantains and cooking bananas (ND)"},
                {"Code": "01.1.7.6", "Description": "Pulses (ND)"},
                {"Code": "01.1.7.7", "Description": "Other vegetables, tubers, plantains and cooking bananas, dried and dehydrated (ND)"},
                {"Code": "01.1.7.8", "Description": "Vegetables, tubers, plantains and cooking bananas, frozen (ND)"},
                {"Code": "01.1.7.9", "Description": "Vegetables, tubers, plantains, cooking bananas and pulses ground and other preparations (ND)"}
            ]},
            {"Code": "01.1.8", "Description": "Sugar, confectionery and desserts (ND)",
             "Subcategories": [
                {"Code": "01.1.8.1", "Description": "Cane and beet sugar (ND)"},
                {"Code": "01.1.8.2", "Description": "Other sugar and sugar substitutes (ND)"},
                {"Code": "01.1.8.3", "Description": "Jams, fruit jellies, marmalades, fruit purée and pastes, honey (ND)"},
                {"Code": "01.1.8.4", "Description": "Nut purée, nut butter and nut pastes (ND)"},
                {"Code": "01.1.8.5", "Description": "Chocolate, cocoa, and cocoa-based food products (ND)"},
                {"Code": "01.1.8.6", "Description": "Ice, ice cream and sorbet (ND)"},
                {"Code": "01.1.8.9", "Description": "Other sugar confectionery and desserts n.e.c. (ND)"}
            ]},
            {"Code": "01.1.9", "Description": "Ready-made food and other food products n.e.c. (ND)",
             "Subcategories": [
                {"Code": "01.1.9.1", "Description": "Ready-made food (ND)"},
                {"Code": "01.1.9.2", "Description": "Baby food (ND)"},
                {"Code": "01.1.9.3", "Description": "Salt, condiments and sauces (ND)"},
                {"Code": "01.1.9.4", "Description": "Spices, culinary herbs and seeds (ND)"},
                {"Code": "01.1.9.9", "Description": "Other food products n.e.c. (ND)"}
            ]}
         ]},
         {"Code": "01.2", "Description": "NON-ALCOHOLIC BEVERAGES",
          "Subcategories": [
            {"Code": "01.2.1", "Description": "Fruit and vegetable juices (ND)",
             "Subcategories": [
                {"Code": "01.2.1.0", "Description": "Fruit and vegetable juices (ND)"}
             ]},
            {"Code": "01.2.2", "Description": "Coffee and coffee substitutes (ND)",
             "Subcategories": [
                {"Code": "01.2.2.0", "Description": "Coffee and coffee substitutes (ND)"}
             ]},
            {"Code": "01.2.3", "Description": "Tea, maté and other plant products for infusion (ND)",
             "Subcategories": [
                {"Code": "01.2.3.0", "Description": "Tea, maté and other plant products for infusion (ND)"}
             ]},
            {"Code": "01.2.4", "Description": "Cocoa drinks (ND)",
             "Subcategories": [
                {"Code": "01.2.4.0", "Description": "Cocoa drinks (ND)"}
             ]},
            {"Code": "01.2.5", "Description": "Water (ND)",
             "Subcategories": [
                {"Code": "01.2.5.0", "Description": "Water (ND)"}
             ]},
            {"Code": "01.2.6", "Description": "Soft drinks (ND)",
             "Subcategories": [
                {"Code": "01.2.6.0", "Description": "Soft drinks (ND)"}
             ]},
            {"Code": "01.2.9", "Description": "Other non-alcoholic beverages (ND)",
             "Subcategories": [
                {"Code": "01.2.9.0", "Description": "Other non-alcoholic beverages (ND)"}
             ]}
          ]},
         {"Code": "01.3", "Description": "SERVICES FOR PROCESSING PRIMARY GOODS FOR FOOD AND NON-ALCOHOLIC BEVERAGES",
          "Subcategories": [
            {"Code": "01.3.0", "Description": "Services for processing primary goods for food and non-alcoholic beverages (S)",
             "Subcategories": [
                {"Code": "01.3.0.0", "Description": "Services for processing primary goods for food and non-alcoholic beverages (S)"}
             ]}
          ]}
     ]}
  ]
  section_2 = [
    {"Code": "02", "Description": "ALCOHOLIC BEVERAGES, TOBACCO AND NARCOTICS",
     "Subcategories": [
        {"Code": "02.1", "Description": "ALCOHOLIC BEVERAGES",
         "Subcategories": [
            {"Code": "02.1.1", "Description": "Spirits and liquors (ND)",
             "Subcategories": [
                {"Code": "02.1.1.0", "Description": "Spirits and liquors (ND)"}
             ]},
            {"Code": "02.1.2", "Description": "Wine (ND)",
             "Subcategories": [
                {"Code": "02.1.2.1", "Description": "Wine from grapes (ND)"},
                {"Code": "02.1.2.2", "Description": "Wine from other sources (ND)"}
             ]},
            {"Code": "02.1.3", "Description": "Beer (ND)",
             "Subcategories": [
                {"Code": "02.1.3.0", "Description": "Beer (ND)"}
             ]},
            {"Code": "02.1.9", "Description": "Other alcoholic beverages (ND)",
             "Subcategories": [
                {"Code": "02.1.9.0", "Description": "Other alcoholic beverages (ND)"}
             ]}
          ]},
        {"Code": "02.2", "Description": "ALCOHOL PRODUCTION SERVICES",
         "Subcategories": [
            {"Code": "02.2.0", "Description": "Alcohol production services (S)",
             "Subcategories": [
                {"Code": "02.2.0.0", "Description": "Alcohol production services (S)"}
             ]}
          ]},
        {"Code": "02.3", "Description": "TOBACCO",
         "Subcategories": [
            {"Code": "02.3.0", "Description": "Tobacco (ND)",
             "Subcategories": [
                {"Code": "02.3.0.1", "Description": "Cigarettes (ND)"},
                {"Code": "02.3.0.2", "Description": "Cigars (ND)"},
                {"Code": "02.3.0.9", "Description": "Other tobacco products (ND)"}
             ]}
          ]},
        {"Code": "02.4", "Description": "NARCOTICS",
         "Subcategories": [
            {"Code": "02.4.0", "Description": "Narcotics (ND)",
             "Subcategories": [
                {"Code": "02.4.0.0", "Description": "Narcotics (ND)"}
             ]}
          ]}
     ]}
]
  section_3 = [
    {"Code": "03", "Description": "Clothing and footwear",
     "Subcategories": [
         {"Code": "03.1", "Description": "Clothing",
          "Subcategories": [
              {"Code": "03.1.1", "Description": "Clothing materials (SD)",
               "Subcategories": [
                   {"Code": "03.1.1.0", "Description": "Clothing materials (SD)"}
               ]},
              {"Code": "03.1.2", "Description": "Garments (SD)",
               "Subcategories": [
                   {"Code": "03.1.2.1", "Description": "Garments for men or boys (SD)"},
                   {"Code": "03.1.2.2", "Description": "Garments for women or girls (SD)"},
                   {"Code": "03.1.2.3", "Description": "Garments for infants (0 to under 2 years) (SD)"},
                   {"Code": "03.1.2.4", "Description": "School uniforms (SD)"}
               ]},
              {"Code": "03.1.3", "Description": "Other articles of clothing and clothing accessories (SD)",
               "Subcategories": [
                   {"Code": "03.1.3.1", "Description": "Other articles of clothing (SD)"},
                   {"Code": "03.1.3.2", "Description": "Clothing accessories (SD)"}
               ]},
              {"Code": "03.1.4", "Description": "Cleaning, repair, tailoring and hire of clothing (S)",
               "Subcategories": [
                   {"Code": "03.1.4.1", "Description": "Cleaning of clothing (S)"},
                   {"Code": "03.1.4.2", "Description": "Repair, tailoring and hire of clothing (S)"}
               ]}
          ]},
         {"Code": "03.2", "Description": "Footwear",
          "Subcategories": [
              {"Code": "03.2.1", "Description": "Shoes and other footwear (SD)",
               "Subcategories": [
                   {"Code": "03.2.1.1", "Description": "Footwear for men (SD)"},
                   {"Code": "03.2.1.2", "Description": "Footwear for women (SD)"},
                   {"Code": "03.2.1.3", "Description": "Footwear for infants and children (SD)"}
               ]},
              {"Code": "03.2.2", "Description": "Cleaning, repair, and hire of footwear (S)",
               "Subcategories": [
                   {"Code": "03.2.2.0", "Description": "Cleaning, repair, and hire of footwear (S)"}
               ]}
          ]}
     ]}
]
  section_4 = [
    {"Code": "04", "Description": "Housing, water, electricity, gas and other fuels",
     "Subcategories": [
         {"Code": "04.1", "Description": "Actual rentals for housing",
          "Subcategories": [
              {"Code": "04.1.1", "Description": "Actual rentals paid by tenants for main residence (S)",
               "Subcategories": [
                   {"Code": "04.1.1.0", "Description": "Actual rentals paid by tenants for main residence (S)"}
               ]},
              {"Code": "04.1.2", "Description": "Other actual rentals (S)",
               "Subcategories": [
                   {"Code": "04.1.2.1", "Description": "Actual rentals paid by tenants for secondary residences (S)"},
                   {"Code": "04.1.2.2", "Description": "Garage rentals and other rentals paid by tenants (S)"}
               ]}
          ]},
         {"Code": "04.2", "Description": "Imputed rentals for housing",
          "Subcategories": [
              {"Code": "04.2.1", "Description": "Imputed rentals of owner-occupiers for main residence (S)",
               "Subcategories": [
                   {"Code": "04.2.1.0", "Description": "Imputed rentals of owner-occupiers for main residence (S)"}
               ]},
              {"Code": "04.2.2", "Description": "Other imputed rentals (S)",
               "Subcategories": [
                   {"Code": "04.2.2.0", "Description": "Other imputed rentals (S)"}
               ]}
          ]},
         {"Code": "04.3", "Description": "Maintenance, repair and security of the dwelling",
          "Subcategories": [
              {"Code": "04.3.1", "Description": "Security equipment and materials for the maintenance and repair of the dwelling (ND)",
               "Subcategories": [
                   {"Code": "04.3.1.1", "Description": "Materials for the maintenance and repair of the dwelling (ND)"},
                   {"Code": "04.3.1.2", "Description": "Security equipment (SD)"}
               ]},
              {"Code": "04.3.2", "Description": "Services for the maintenance, repair and security of the dwelling (S)",
               "Subcategories": [
                   {"Code": "04.3.2.0", "Description": "Services for the maintenance, repair and security of the dwelling (S)"}
               ]}
          ]},
         {"Code": "04.4", "Description": "Water supply and miscellaneous services relating to the dwelling",
          "Subcategories": [
              {"Code": "04.4.1", "Description": "Water supply (ND)",
               "Subcategories": [
                   {"Code": "04.4.1.1", "Description": "Water supply through network systems (ND)"},
                   {"Code": "04.4.1.2", "Description": "Water supply through other systems (ND)"}
               ]},
              {"Code": "04.4.2", "Description": "Refuse collection (S)",
               "Subcategories": [
                   {"Code": "04.4.2.0", "Description": "Refuse collection (S)"}
               ]},
              {"Code": "04.4.3", "Description": "Sewage collection (S)",
               "Subcategories": [
                   {"Code": "04.4.3.1", "Description": "Sewage collection through sewer systems (S)"},
                   {"Code": "04.4.3.2", "Description": "Sewage collection through onsite sanitation systems (S)"}
               ]},
              {"Code": "04.4.4", "Description": "Other services relating to the dwelling n.e.c. (S)",
               "Subcategories": [
                   {"Code": "04.4.4.1", "Description": "Maintenance charges in multi-occupied buildings (S)"},
                   {"Code": "04.4.4.9", "Description": "Other services related to dwelling (S)"}
               ]}
          ]},
         {"Code": "04.5", "Description": "Electricity, gas and other fuels",
          "Subcategories": [
              {"Code": "04.5.1", "Description": "Electricity (ND)",
               "Subcategories": [
                   {"Code": "04.5.1.0", "Description": "Electricity (ND)"}
               ]},
              {"Code": "04.5.2", "Description": "Gas (ND)",
               "Subcategories": [
                   {"Code": "04.5.2.1", "Description": "Natural gas through networks (ND)"},
                   {"Code": "04.5.2.2", "Description": "Liquefied hydrocarbons (ND)"}
               ]},
              {"Code": "04.5.3", "Description": "Liquid fuels (ND)",
               "Subcategories": [
                   {"Code": "04.5.3.0", "Description": "Liquid fuels (ND)"}
               ]},
              {"Code": "04.5.4", "Description": "Solid fuels (ND)",
               "Subcategories": [
                   {"Code": "04.5.4.1", "Description": "Coal, coal briquettes and peat (ND)"},
                   {"Code": "04.5.4.2", "Description": "Wood fuel, including pellets and briquettes (ND)"},
                   {"Code": "04.5.4.3", "Description": "Charcoal (ND)"},
                   {"Code": "04.5.4.9", "Description": "Other solid fuels (ND)"}
               ]},
              {"Code": "04.5.5", "Description": "Other energy for heating and cooling (ND)",
               "Subcategories": [
                   {"Code": "04.5.5.0", "Description": "Other energy for heating and cooling (ND)"}
               ]}
          ]}
     ]}
]
  section_5 = [
    {"Code": "05", "Description": "Furnishings, household equipment and routine household maintenance",
     "Subcategories": [
         {"Code": "05.1", "Description": "Furniture, furnishings, and loose carpets",
          "Subcategories": [
              {"Code": "05.1.1", "Description": "Furniture, furnishings and loose carpets (D)",
               "Subcategories": [
                   {"Code": "05.1.1.1", "Description": "Household furniture (D)"},
                   {"Code": "05.1.1.2", "Description": "Garden and camping furniture (D)"},
                   {"Code": "05.1.1.3", "Description": "Lighting equipment (D)"},
                   {"Code": "05.1.1.4", "Description": "Furnishings, loose carpets and rugs (D)"}
               ]},
              {"Code": "05.1.2", "Description": "Repair, installation and hire of furniture, furnishings and loose carpets (S)",
               "Subcategories": [
                   {"Code": "05.1.2.0", "Description": "Repair, installation and hire of furniture, furnishings and loose carpets (S)"}
               ]}
          ]},
         {"Code": "05.2", "Description": "Household textiles",
          "Subcategories": [
              {"Code": "05.2.1", "Description": "Household textiles (SD)",
               "Subcategories": [
                   {"Code": "05.2.1.1", "Description": "Furnishing fabrics and curtains (SD)"},
                   {"Code": "05.2.1.2", "Description": "Bed linen and bedding (SD)"},
                   {"Code": "05.2.1.3", "Description": "Table linen and bathroom linen (SD)"},
                   {"Code": "05.2.1.9", "Description": "Other household textiles (SD)"}
               ]},
              {"Code": "05.2.2", "Description": "Repair, hire and sewing services of household textiles (S)",
               "Subcategories": [
                   {"Code": "05.2.2.0", "Description": "Repair, hire and sewing services of household textiles (S)"}
               ]}
          ]},
         {"Code": "05.3", "Description": "Household appliances",
          "Subcategories": [
              {"Code": "05.3.1", "Description": "Major household appliances, whether electric or not (D)",
               "Subcategories": [
                   {"Code": "05.3.1.1", "Description": "Major kitchen appliances (D)"},
                   {"Code": "05.3.1.2", "Description": "Major laundry appliances (D)"},
                   {"Code": "05.3.1.3", "Description": "Heaters, air conditioners (D)"},
                   {"Code": "05.3.1.4", "Description": "Cleaning equipment (D)"},
                   {"Code": "05.3.1.9", "Description": "Other major household appliances (D)"}
               ]},
              {"Code": "05.3.2", "Description": "Small household appliances (SD)",
               "Subcategories": [
                   {"Code": "05.3.2.1", "Description": "Small appliances for cooking and processing of food (SD)"},
                   {"Code": "05.3.2.2", "Description": "Small appliances for preparing beverages (SD)"},
                   {"Code": "05.3.2.9", "Description": "Other small household appliances (SD)"}
               ]},
              {"Code": "05.3.3", "Description": "Repair, installation and hire of household appliances (S)",
               "Subcategories": [
                   {"Code": "05.3.3.0", "Description": "Repair, installation and hire of household appliances (S)"}
               ]}
          ]},
         {"Code": "05.4", "Description": "Glassware, tableware and household utensils",
          "Subcategories": [
              {"Code": "05.4.0", "Description": "Glassware, tableware and household utensils (SD)",
               "Subcategories": [
                   {"Code": "05.4.0.1", "Description": "Glassware, crystal-ware, ceramic ware and chinaware (SD)"},
                   {"Code": "05.4.0.2", "Description": "Cutlery, flatware and silverware (SD)"},
                   {"Code": "05.4.0.3", "Description": "Kitchen utensils and articles (SD)"},
                   {"Code": "05.4.0.4", "Description": "Repair and hire of glassware, tableware and household utensils (S)"}
               ]}
          ]},
         {"Code": "05.5", "Description": "Tools and equipment for house and garden",
          "Subcategories": [
              {"Code": "05.5.1", "Description": "Motorized tools and equipment (D)",
               "Subcategories": [
                   {"Code": "05.5.1.0", "Description": "Motorized tools and equipment (D)"}
               ]},
              {"Code": "05.5.2", "Description": "Non-motorized tools and miscellaneous accessories (SD)",
               "Subcategories": [
                   {"Code": "05.5.2.1", "Description": "Non-motorized tools (SD)"},
                   {"Code": "05.5.2.2", "Description": "Miscellaneous accessories (SD)"}
               ]},
              {"Code": "05.5.3", "Description": "Repair and hire of motorized and non-motorized tools and equipment (S)",
               "Subcategories": [
                   {"Code": "05.5.3.0", "Description": "Repair and hire of motorized and non-motorized tools and equipment (S)"}
               ]}
          ]},
         {"Code": "05.6", "Description": "Goods and services for routine household maintenance",
          "Subcategories": [
              {"Code": "05.6.1", "Description": "Non-durable household goods (ND)",
               "Subcategories": [
                   {"Code": "05.6.1.1", "Description": "Household cleaning and maintenance products (ND)"},
                   {"Code": "05.6.1.9", "Description": "Other non-durable household goods (ND)"}
               ]},
              {"Code": "05.6.2", "Description": "Domestic services and household services (S)",
               "Subcategories": [
                   {"Code": "05.6.2.1", "Description": "Domestic services by paid staff (S)"},
                   {"Code": "05.6.2.9", "Description": "Other household services (S)"}
               ]}
          ]}
     ]}
]
  section_6 = [
    {"Code": "06", "Description": "Health",
     "Subcategories": [
         {"Code": "06.1", "Description": "Medicines and health products",
          "Subcategories": [
              {"Code": "06.1.1", "Description": "Medicines (ND)",
               "Subcategories": [
                   {"Code": "06.1.1.1", "Description": "Medicines, vaccines and other pharmaceutical preparations (ND)"},
                   {"Code": "06.1.1.2", "Description": "Herbal medicines and homeopathic products (ND)"}
               ]},
              {"Code": "06.1.2", "Description": "Medical products (ND)",
               "Subcategories": [
                   {"Code": "06.1.2.1", "Description": "Medical diagnostic products (ND)"},
                   {"Code": "06.1.2.2", "Description": "Prevention and protective devices (ND)"},
                   {"Code": "06.1.2.3", "Description": "Treatment devices for personal use (ND)"}
               ]},
              {"Code": "06.1.3", "Description": "Assistive products (D)",
               "Subcategories": [
                   {"Code": "06.1.3.1", "Description": "Assistive products for vision (D)"},
                   {"Code": "06.1.3.2", "Description": "Assistive products for hearing and communication (D)"},
                   {"Code": "06.1.3.3", "Description": "Assistive products for mobility and daily living (D)"}
               ]},
              {"Code": "06.1.4", "Description": "Repair, rental and maintenance of medical and assistive products (S)",
               "Subcategories": [
                   {"Code": "06.1.4.0", "Description": "Repair, rental and maintenance of medical and assistive products (S)"}
               ]}
          ]},
         {"Code": "06.2", "Description": "Outpatient care services",
          "Subcategories": [
              {"Code": "06.2.1", "Description": "Preventive care services (S)",
               "Subcategories": [
                   {"Code": "06.2.1.1", "Description": "Immunization services (S)"},
                   {"Code": "06.2.1.9", "Description": "Other preventive services (S)"}
               ]},
              {"Code": "06.2.2", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "06.2.2.1", "Description": "Dental preventive services (S)"},
                   {"Code": "06.2.2.9", "Description": "Other outpatient dental services (S)"}
               ]},
              {"Code": "06.2.3", "Description": "Other outpatient care services (S)",
               "Subcategories": [
                   {"Code": "06.2.3.1", "Description": "Outpatient curative and rehabilitative services (S)"},
                   {"Code": "06.2.3.2", "Description": "Outpatient long-term care services (S)"}
               ]}
          ]},
         {"Code": "06.3", "Description": "Inpatient care services",
          "Subcategories": [
              {"Code": "06.3.1", "Description": "Inpatient curative and rehabilitative services (S)",
               "Subcategories": [
                   {"Code": "06.3.1.0", "Description": "Inpatient curative and rehabilitative services (S)"}
               ]},
              {"Code": "06.3.2", "Description": "Inpatient long-term care services (S)",
               "Subcategories": [
                   {"Code": "06.3.2.0", "Description": "Inpatient long-term care services (S)"}
               ]}
          ]},
         {"Code": "06.4", "Description": "Other health services",
          "Subcategories": [
              {"Code": "06.4.1", "Description": "Diagnostic imaging services and medical laboratory services (S)",
               "Subcategories": [
                   {"Code": "06.4.1.0", "Description": "Diagnostic imaging services and medical laboratory services (S)"}
               ]},
              {"Code": "06.4.2", "Description": "Patient emergency transportation services and emergency rescue (S)",
               "Subcategories": [
                   {"Code": "06.4.2.0", "Description": "Patient emergency transportation services and emergency rescue (S)"}
               ]}
          ]}
     ]}
]
  section_7 = [
    {"Code": "07", "Description": "Transport",
     "Subcategories": [
         {"Code": "07.1", "Description": "Purchase of vehicles",
          "Subcategories": [
              {"Code": "07.1.1", "Description": "Motor cars (D)",
               "Subcategories": [
                   {"Code": "07.1.1.1", "Description": "New motor cars (D)"},
                   {"Code": "07.1.1.2", "Description": "Second-hand motor cars (D)"}
               ]},
              {"Code": "07.1.2", "Description": "Motorcycles (D)",
               "Subcategories": [
                   {"Code": "07.1.2.0", "Description": "Motorcycles (D)"}
               ]},
              {"Code": "07.1.3", "Description": "Bicycles (D)",
               "Subcategories": [
                   {"Code": "07.1.3.0", "Description": "Bicycles (D)"}
               ]},
              {"Code": "07.1.4", "Description": "Animal drawn vehicles (D)",
               "Subcategories": [
                   {"Code": "07.1.4.0", "Description": "Animal drawn vehicles (D)"}
               ]}
          ]},
         {"Code": "07.2", "Description": "Operation of personal transport equipment",
          "Subcategories": [
              {"Code": "07.2.1", "Description": "Parts and accessories for personal transport equipment (SD)",
               "Subcategories": [
                   {"Code": "07.2.1.1", "Description": "Tyres (SD)"},
                   {"Code": "07.2.1.2", "Description": "Parts for personal transport equipment (SD)"},
                   {"Code": "07.2.1.3", "Description": "Accessories for personal transport equipment (SD)"}
               ]},
              {"Code": "07.2.2", "Description": "Fuels and lubricants for personal transport equipment (ND)",
               "Subcategories": [
                   {"Code": "07.2.2.1", "Description": "Diesel (ND)"},
                   {"Code": "07.2.2.2", "Description": "Petrol (ND)"},
                   {"Code": "07.2.2.3", "Description": "Other fuels for personal transport equipment (ND)"},
                   {"Code": "07.2.2.4", "Description": "Lubricants (ND)"}
               ]},
              {"Code": "07.2.3", "Description": "Maintenance and repair of personal transport equipment (S)",
               "Subcategories": [
                   {"Code": "07.2.3.0", "Description": "Maintenance and repair of personal transport equipment (S)"}
               ]},
              {"Code": "07.2.4", "Description": "Other services in respect of personal transport equipment (S)",
               "Subcategories": [
                   {"Code": "07.2.4.1", "Description": "Services for parking (S)"},
                   {"Code": "07.2.4.2", "Description": "Toll facilities (S)"},
                   {"Code": "07.2.4.3", "Description": "Driving lessons, tests, licences, and roadworthiness tests (S)"},
                   {"Code": "07.2.4.4", "Description": "Hire of personal transport equipment without driver (S)"}
               ]}
          ]},
         {"Code": "07.3", "Description": "Passenger transport services",
          "Subcategories": [
              {"Code": "07.3.1", "Description": "Passenger transport by railway (S)",
               "Subcategories": [
                   {"Code": "07.3.1.1", "Description": "Passenger transport by train (S)"},
                   {"Code": "07.3.1.2", "Description": "Passenger transport by rapid transit and tram (S)"}
               ]},
              {"Code": "07.3.2", "Description": "Passenger transport by road (S)",
               "Subcategories": [
                   {"Code": "07.3.2.1", "Description": "Passenger transport by bus and coach (S)"},
                   {"Code": "07.3.2.2", "Description": "Passenger transport by taxi and hired car with driver (S)"},
                   {"Code": "07.3.2.3", "Description": "Passenger transport for students to and from school (S)"},
                   {"Code": "07.3.2.9", "Description": "Other passenger transport by road (S)"}
               ]},
              {"Code": "07.3.3", "Description": "Passenger transport by air (S)",
               "Subcategories": [
                   {"Code": "07.3.3.1", "Description": "Passenger transport by air, domestic (S)"},
                   {"Code": "07.3.3.2", "Description": "Passenger transport by air, international (S)"}
               ]},
              {"Code": "07.3.4", "Description": "Passenger transport by sea and inland waterway (S)",
               "Subcategories": [
                   {"Code": "07.3.4.0", "Description": "Passenger transport by sea and inland waterway (S)"}
               ]},
              {"Code": "07.3.5", "Description": "Combined passenger transport (S)",
               "Subcategories": [
                   {"Code": "07.3.5.0", "Description": "Combined passenger transport (S)"}
               ]},
              {"Code": "07.3.6", "Description": "Other purchased transport services (S)",
               "Subcategories": [
                   {"Code": "07.3.6.0", "Description": "Other purchased transport services (S)"}
               ]}
          ]},
         {"Code": "07.4", "Description": "Transport services of goods",
          "Subcategories": [
              {"Code": "07.4.1", "Description": "Postal and courier services (S)",
               "Subcategories": [
                   {"Code": "07.4.1.1", "Description": "Letter handling services (S)"},
                   {"Code": "07.4.1.2", "Description": "Courier and parcel delivery services (S)"}
               ]},
              {"Code": "07.4.9", "Description": "Other transport of goods (S)",
               "Subcategories": [
                   {"Code": "07.4.9.1", "Description": "Removal and storage services (S)"},
                   {"Code": "07.4.9.2", "Description": "Delivery of goods (S)"}
               ]}
          ]}
     ]}
]
  section_8 = [
    {"Code": "08", "Description": "Information and communication",
     "Subcategories": [
         {"Code": "08.1", "Description": "Information and communication equipment",
          "Subcategories": [
              {"Code": "08.1.1", "Description": "Fixed telephone equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.1.0", "Description": "Fixed telephone equipment (D)"}
               ]},
              {"Code": "08.1.2", "Description": "Mobile telephone equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.2.0", "Description": "Mobile telephone equipment (D)"}
               ]},
              {"Code": "08.1.3", "Description": "Information processing equipment (D)",
               "Subcategories": [
                   {"Code": "08.1.3.1", "Description": "Computers, laptops and tablets (D)"},
                   {"Code": "08.1.3.2", "Description": "Peripheral equipment and its consumable components (D)"}
               ]},
              {"Code": "08.1.4", "Description": "Equipment for the reception, recording and reproduction of sound and vision (D)",
               "Subcategories": [
                   {"Code": "08.1.4.0", "Description": "Equipment for the reception, recording and reproduction of sound and vision (D)"}
               ]},
              {"Code": "08.1.5", "Description": "Unrecorded recording media (SD)",
               "Subcategories": [
                   {"Code": "08.1.5.0", "Description": "Unrecorded recording media (SD)"}
               ]},
              {"Code": "08.1.9", "Description": "Other information and communication equipment and accessories (D)",
               "Subcategories": [
                   {"Code": "08.1.9.1", "Description": "Other information and communication equipment (D)"},
                   {"Code": "08.1.9.2", "Description": "Other information and communication accessories (SD)"}
               ]}
          ]},
         {"Code": "08.2", "Description": "Software excluding games",
          "Subcategories": [
              {"Code": "08.2.0", "Description": "Software (S)",
               "Subcategories": [
                   {"Code": "08.2.0.0", "Description": "Software (S)"}
               ]}
          ]},
         {"Code": "08.3", "Description": "Information and communication services",
          "Subcategories": [
              {"Code": "08.3.1", "Description": "Fixed communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.1.0", "Description": "Fixed communication services (S)"}
               ]},
              {"Code": "08.3.2", "Description": "Mobile communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.2.0", "Description": "Mobile communication services (S)"}
               ]},
              {"Code": "08.3.3", "Description": "Internet access provision services and net storage services (S)",
               "Subcategories": [
                   {"Code": "08.3.3.0", "Description": "Internet access provision services and net storage services (S)"}
               ]},
              {"Code": "08.3.4", "Description": "Bundled telecommunication services (S)",
               "Subcategories": [
                   {"Code": "08.3.4.0", "Description": "Bundled telecommunication services (S)"}
               ]},
              {"Code": "08.3.5", "Description": "Repair and rental of information and communication equipment (S)",
               "Subcategories": [
                   {"Code": "08.3.5.0", "Description": "Repair and rental of information and communication equipment (S)"}
               ]},
              {"Code": "08.3.9", "Description": "Other information and communication services (S)",
               "Subcategories": [
                   {"Code": "08.3.9.1", "Description": "TV and radio licences and fees (S)"},
                   {"Code": "08.3.9.2", "Description": "Subscription to audio-visual content, streaming services and rentals of audio-visual content (S)"},
                   {"Code": "08.3.9.9", "Description": "Other information and communication services (S)"}
               ]}
          ]}
     ]}
]
  section_9 = [
    {"Code": "09", "Description": "Recreation, sport and culture",
     "Subcategories": [
         {"Code": "09.1", "Description": "Recreational durables",
          "Subcategories": [
              {"Code": "09.1.1", "Description": "Photographic and cinematographic equipment and optical instruments (D)",
               "Subcategories": [
                   {"Code": "09.1.1.1", "Description": "Cameras (D)"},
                   {"Code": "09.1.1.2", "Description": "Accessories for photographic and cinematographic equipment (D)"},
                   {"Code": "09.1.1.3", "Description": "Optical instruments (D)"}
               ]},
              {"Code": "09.1.2", "Description": "Major durables for recreation (D)",
               "Subcategories": [
                   {"Code": "09.1.2.1", "Description": "Camper vans, caravans and trailers (D)"},
                   {"Code": "09.1.2.2", "Description": "Aeroplanes, microlight aircraft, gliders, hang gliders and hot-air balloons (D)"},
                   {"Code": "09.1.2.3", "Description": "Boats, yachts, outboard motors and other water sport equipment (D)"},
                   {"Code": "09.1.2.4", "Description": "Horses, ponies, camel and dromedaries and accessories (D)"},
                   {"Code": "09.1.2.9", "Description": "Other major durables for recreation (D)"}
               ]}
          ]},
         {"Code": "09.2", "Description": "Other recreational goods",
          "Subcategories": [
              {"Code": "09.2.1", "Description": "Games, toys and hobbies (SD)",
               "Subcategories": [
                   {"Code": "09.2.1.1", "Description": "Video game computers, game consoles, game apps and software (SD)"},
                   {"Code": "09.2.1.2", "Description": "Other games, toys and hobbies (SD)"},
                   {"Code": "09.2.1.3", "Description": "Celebration articles (ND)"}
               ]},
              {"Code": "09.2.2", "Description": "Equipment for sport, camping and open-air recreation (SD)",
               "Subcategories": [
                   {"Code": "09.2.2.1", "Description": "Equipment for sport (SD)"},
                   {"Code": "09.2.2.2", "Description": "Equipment for camping and open-air recreation (SD)"}
               ]}
          ]},
         {"Code": "09.3", "Description": "Garden products and pets",
          "Subcategories": [
              {"Code": "09.3.1", "Description": "Garden products, plants and flowers (ND)",
               "Subcategories": [
                   {"Code": "09.3.1.1", "Description": "Garden products (ND)"},
                   {"Code": "09.3.1.2", "Description": "Plants, seeds and flowers (ND)"}
               ]},
              {"Code": "09.3.2", "Description": "Pets and products for pets (ND)",
               "Subcategories": [
                   {"Code": "09.3.2.1", "Description": "Purchase of pets (ND)"},
                   {"Code": "09.3.2.2", "Description": "Products for pets and other household animals (ND)"}
               ]}
          ]},
         {"Code": "09.4", "Description": "Recreational services",
          "Subcategories": [
              {"Code": "09.4.1", "Description": "Hire and repair of photographic and cinematographic equipment and optical instruments (S)",
               "Subcategories": [
                   {"Code": "09.4.1.0", "Description": "Hire and repair of photographic and cinematographic equipment and optical instruments (S)"}
               ]},
              {"Code": "09.4.2", "Description": "Hire, maintenance and repair of major durables for recreation (S)",
               "Subcategories": [
                   {"Code": "09.4.2.1", "Description": "Hire, maintenance and repair of camper vans and caravans (S)"},
                   {"Code": "09.4.2.2", "Description": "Hire, maintenance and repair of other major durables for recreation (S)"}
               ]},
              {"Code": "09.4.3", "Description": "Hire and repair of games, toys and hobbies (S)",
               "Subcategories": [
                   {"Code": "09.4.3.1", "Description": "Rental of game software and subscription to online games (S)"},
                   {"Code": "09.4.3.2", "Description": "Rental and repair of games, toys and hobbies (S)"}
               ]},
              {"Code": "09.4.4", "Description": "Hire and repair of equipment for sport, camping and open-air recreation (S)",
               "Subcategories": [
                   {"Code": "09.4.4.0", "Description": "Hire and repair of equipment for sport, camping and open-air recreation (S)"}
               ]},
              {"Code": "09.4.5", "Description": "Veterinary and other services for pets (S)",
               "Subcategories": [
                   {"Code": "09.4.5.0", "Description": "Veterinary and other services for pets (S)"}
               ]},
              {"Code": "09.4.6", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "09.4.6.1", "Description": "Recreational and leisure services (S)"},
                   {"Code": "09.4.6.2", "Description": "Sporting services - practice (S)"},
                   {"Code": "09.4.6.3", "Description": "Sporting services - attendance (S)"}
               ]},
              {"Code": "09.4.7", "Description": "Games of chance (S)",
               "Subcategories": [
                   {"Code": "09.4.7.0", "Description": "Games of chance (S)"}
               ]}
          ]},
         {"Code": "09.5", "Description": "Cultural goods",
          "Subcategories": [
              {"Code": "09.5.1", "Description": "Musical instruments (D)",
               "Subcategories": [
                   {"Code": "09.5.1.0", "Description": "Musical instruments (D)"}
               ]},
              {"Code": "09.5.2", "Description": "Audio-visual media (SD)",
               "Subcategories": [
                   {"Code": "09.5.2.0", "Description": "Audio-visual media (SD)"}
               ]}
          ]},
         {"Code": "09.6", "Description": "Cultural services",
          "Subcategories": [
              {"Code": "09.6.1", "Description": "Services provided by cinemas, theatres and concert venues (S)",
               "Subcategories": [
                   {"Code": "09.6.1.0", "Description": "Services provided by cinemas, theatres and concert venues (S)"}
               ]},
              {"Code": "09.6.2", "Description": "Services provided by museums, libraries, and cultural sites (S)",
               "Subcategories": [
                   {"Code": "09.6.2.0", "Description": "Services provided by museums, libraries, and cultural sites (S)"}
               ]},
              {"Code": "09.6.3", "Description": "Photographic services (S)",
               "Subcategories": [
                   {"Code": "09.6.3.0", "Description": "Photographic services (S)"}
               ]},
              {"Code": "09.6.9", "Description": "Other cultural services (S)",
               "Subcategories": [
                   {"Code": "09.6.9.0", "Description": "Other cultural services (S)"}
               ]}
          ]},
         {"Code": "09.7", "Description": "Newspapers, books and stationery",
          "Subcategories": [
              {"Code": "09.7.1", "Description": "Books (SD)",
               "Subcategories": [
                   {"Code": "09.7.1.1", "Description": "Educational and text books (SD)"},
                   {"Code": "09.7.1.9", "Description": "Other books (SD)"}
               ]},
              {"Code": "09.7.2", "Description": "Newspapers and periodicals (ND)",
               "Subcategories": [
                   {"Code": "09.7.2.1", "Description": "Newspapers (ND)"},
                   {"Code": "09.7.2.2", "Description": "Magazines and periodicals (ND)"}
               ]},
              {"Code": "09.7.3", "Description": "Miscellaneous printed matter (ND)",
               "Subcategories": [
                   {"Code": "09.7.3.0", "Description": "Miscellaneous printed matter (ND)"}
               ]},
              {"Code": "09.7.4", "Description": "Stationery and drawing materials (ND)",
               "Subcategories": [
                   {"Code": "09.7.4.0", "Description": "Stationery and drawing materials (ND)"}
               ]}
          ]},
         {"Code": "09.8", "Description": "Package holidays",
          "Subcategories": [
              {"Code": "09.8.0", "Description": "Package holidays (S)",
               "Subcategories": [
                   {"Code": "09.8.0.0", "Description": "Package holidays (S)"}
               ]}
          ]}
     ]}
]
  section_10 = [
    {"Code": "10", "Description": "Education services",
     "Subcategories": [
         {"Code": "10.1", "Description": "Early childhood and primary education",
          "Subcategories": [
              {"Code": "10.1.0", "Description": "Early childhood and primary education (S)",
               "Subcategories": [
                   {"Code": "10.1.0.1", "Description": "Early childhood education (S)"},
                   {"Code": "10.1.0.2", "Description": "Primary education (S)"}
               ]}
          ]},
         {"Code": "10.2", "Description": "Secondary education",
          "Subcategories": [
              {"Code": "10.2.0", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "10.2.0.0", "Description": "Secondary education (S)"}
               ]}
          ]},
         {"Code": "10.3", "Description": "Post-secondary non-tertiary education",
          "Subcategories": [
              {"Code": "10.3.0", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "10.3.0.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]}
          ]},
         {"Code": "10.4", "Description": "Tertiary education",
          "Subcategories": [
              {"Code": "10.4.0", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "10.4.0.0", "Description": "Tertiary education (S)"}
               ]}
          ]},
         {"Code": "10.5", "Description": "Education not defined by level",
          "Subcategories": [
              {"Code": "10.5.0", "Description": "Education not defined by level (S)",
               "Subcategories": [
                   {"Code": "10.5.0.1", "Description": "Tutoring (S)"},
                   {"Code": "10.5.0.9", "Description": "Other education not defined by level (S)"}
               ]}
          ]}
     ]}
]
  section_11 = [
    {"Code": "11", "Description": "Restaurants and accommodation services",
     "Subcategories": [
         {"Code": "11.1", "Description": "Food and beverage serving services",
          "Subcategories": [
              {"Code": "11.1.1", "Description": "Restaurants, cafés and the like (S)",
               "Subcategories": [
                   {"Code": "11.1.1.1", "Description": "Restaurants, cafés and the like – with full service (S)"},
                   {"Code": "11.1.1.2", "Description": "Restaurants, cafés and the like – with limited service (S)"}
               ]},
              {"Code": "11.1.2", "Description": "Canteens, cafeterias and refectories (S)",
               "Subcategories": [
                   {"Code": "11.1.2.1", "Description": "Canteens, cafeterias of universities, schools, and kindergartens (S)"},
                   {"Code": "11.1.2.9", "Description": "Other canteens, cafeterias and refectories (S)"}
               ]}
          ]},
         {"Code": "11.2", "Description": "Accommodation services",
          "Subcategories": [
              {"Code": "11.2.0", "Description": "Accommodation services (S)",
               "Subcategories": [
                   {"Code": "11.2.0.1", "Description": "Hotels, motels, inns and similar accommodation services (S)"},
                   {"Code": "11.2.0.2", "Description": "Holiday centres, camping sites, youth hostels and similar accommodation services (S)"},
                   {"Code": "11.2.0.3", "Description": "Accommodation services of boarding schools, universities and other educational establishments (S)"},
                   {"Code": "11.2.0.9", "Description": "Other accommodation services (S)"}
               ]}
          ]}
     ]}
]
  section_12 = [
    {"Code": "12", "Description": "Insurance and financial services",
     "Subcategories": [
         {"Code": "12.1", "Description": "Insurance",
          "Subcategories": [
              {"Code": "12.1.1", "Description": "Life and accident insurance (S)",
               "Subcategories": [
                   {"Code": "12.1.1.0", "Description": "Life and accident insurance (S)"}
               ]},
              {"Code": "12.1.2", "Description": "Insurance connected with health (S)",
               "Subcategories": [
                   {"Code": "12.1.2.0", "Description": "Insurance connected with health (S)"}
               ]},
              {"Code": "12.1.3", "Description": "Insurance connected with the dwelling (S)",
               "Subcategories": [
                   {"Code": "12.1.3.0", "Description": "Insurance connected with the dwelling (S)"}
               ]},
              {"Code": "12.1.4", "Description": "Insurance connected with transport (S)",
               "Subcategories": [
                   {"Code": "12.1.4.1", "Description": "Personal transport insurance (S)"},
                   {"Code": "12.1.4.2", "Description": "Travel insurance (S)"}
               ]},
              {"Code": "12.1.9", "Description": "Other insurance (S)",
               "Subcategories": [
                   {"Code": "12.1.9.0", "Description": "Other insurance (S)"}
               ]}
          ]},
         {"Code": "12.2", "Description": "Financial services",
          "Subcategories": [
              {"Code": "12.2.1", "Description": "Financial intermediation services indirectly measured (S)",
               "Subcategories": [
                   {"Code": "12.2.1.0", "Description": "Financial intermediation services indirectly measured (S)"}
               ]},
              {"Code": "12.2.2", "Description": "Explicit charges by deposit-taking corporations (S)",
               "Subcategories": [
                   {"Code": "12.2.2.0", "Description": "Explicit charges by deposit-taking corporations (S)"}
               ]},
              {"Code": "12.2.9", "Description": "Other financial services (S)",
               "Subcategories": [
                   {"Code": "12.2.9.1", "Description": "Remittances fees (S)"},
                   {"Code": "12.2.9.9", "Description": "Other financial services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_13 = [
    {"Code": "13", "Description": "Personal care, social protection, and miscellaneous goods and services",
     "Subcategories": [
         {"Code": "13.1", "Description": "Personal care",
          "Subcategories": [
              {"Code": "13.1.1", "Description": "Electric appliances for personal care (SD)",
               "Subcategories": [
                   {"Code": "13.1.1.1", "Description": "Electric appliances for personal care (SD)"},
                   {"Code": "13.1.1.2", "Description": "Repair of electric appliances for personal care (S)"}
               ]},
              {"Code": "13.1.2", "Description": "Other appliances, articles, and products for personal care (ND)",
               "Subcategories": [
                   {"Code": "13.1.2.0", "Description": "Other appliances, articles, and products for personal care (ND)"}
               ]},
              {"Code": "13.1.3", "Description": "Hairdressing salons and personal grooming establishments (S)",
               "Subcategories": [
                   {"Code": "13.1.3.1", "Description": "Hairdressing (S)"},
                   {"Code": "13.1.3.2", "Description": "Personal grooming treatments (S)"}
               ]}
          ]},
         {"Code": "13.2", "Description": "Other personal effects",
          "Subcategories": [
              {"Code": "13.2.1", "Description": "Jewellery and watches (D)",
               "Subcategories": [
                   {"Code": "13.2.1.1", "Description": "Jewellery and watches (D)"},
                   {"Code": "13.2.1.2", "Description": "Repair and hire of jewellery, clocks, and watches (S)"}
               ]},
              {"Code": "13.2.2", "Description": "Devotional articles and articles for religious and ritual celebrations (SD)",
               "Subcategories": [
                   {"Code": "13.2.2.0", "Description": "Devotional articles and articles for religious and ritual celebrations (SD)"}
               ]},
              {"Code": "13.2.9", "Description": "Other personal effects n.e.c. (SD)",
               "Subcategories": [
                   {"Code": "13.2.9.1", "Description": "Travel goods and articles for babies and other personal effects n.e.c. (SD)"},
                   {"Code": "13.2.9.2", "Description": "Repair or hire of other personal effects n.e.c. (S)"}
               ]}
          ]},
         {"Code": "13.3", "Description": "Social protection",
          "Subcategories": [
              {"Code": "13.3.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "13.3.0.1", "Description": "Child care services (S)"},
                   {"Code": "13.3.0.2", "Description": "Non-medical retirement homes for elderly persons and residences for disabled persons (S)"},
                   {"Code": "13.3.0.3", "Description": "Services to maintain persons in their private homes (S)"},
                   {"Code": "13.3.0.9", "Description": "Other social protection services (S)"}
               ]}
          ]},
         {"Code": "13.9", "Description": "Other services",
          "Subcategories": [
              {"Code": "13.9.0", "Description": "Other services (S)",
               "Subcategories": [
                   {"Code": "13.9.0.1", "Description": "Prostitution (S)"},
                   {"Code": "13.9.0.2", "Description": "Religious services (S)"},
                   {"Code": "13.9.0.9", "Description": "Other services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_14 = [
    {"Code": "14", "Description": "Individual consumption expenditure of non-profit institutions serving households (NPISHs)",
     "Subcategories": [
         {"Code": "14.1", "Description": "Housing",
          "Subcategories": [
              {"Code": "14.1.0", "Description": "Housing (S)",
               "Subcategories": [
                   {"Code": "14.1.0.0", "Description": "Housing (S)"}
               ]}
          ]},
         {"Code": "14.2", "Description": "Health",
          "Subcategories": [
              {"Code": "14.2.1", "Description": "Pharmaceutical products (ND)",
               "Subcategories": [
                   {"Code": "14.2.1.0", "Description": "Pharmaceutical products (ND)"}
               ]},
              {"Code": "14.2.2", "Description": "Other medical products (ND)",
               "Subcategories": [
                   {"Code": "14.2.2.0", "Description": "Other medical products (ND)"}
               ]},
              {"Code": "14.2.3", "Description": "Therapeutic appliances and equipment (D)",
               "Subcategories": [
                   {"Code": "14.2.3.0", "Description": "Therapeutic appliances and equipment (D)"}
               ]},
              {"Code": "14.2.4", "Description": "Outpatient medical services (S)",
               "Subcategories": [
                   {"Code": "14.2.4.0", "Description": "Outpatient medical services (S)"}
               ]},
              {"Code": "14.2.5", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "14.2.5.0", "Description": "Outpatient dental services (S)"}
               ]},
              {"Code": "14.2.6", "Description": "Outpatient paramedical services (S)",
               "Subcategories": [
                   {"Code": "14.2.6.0", "Description": "Outpatient paramedical services (S)"}
               ]},
              {"Code": "14.2.7", "Description": "Hospital services (S)",
               "Subcategories": [
                   {"Code": "14.2.7.0", "Description": "Hospital services (S)"}
               ]},
              {"Code": "14.2.8", "Description": "Other health services (S)",
               "Subcategories": [
                   {"Code": "14.2.8.0", "Description": "Other health services (S)"}
               ]}
          ]},
         {"Code": "14.3", "Description": "Recreation and culture",
          "Subcategories": [
              {"Code": "14.3.1", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "14.3.1.0", "Description": "Recreational and sporting services (S)"}
               ]},
              {"Code": "14.3.2", "Description": "Cultural services (S)",
               "Subcategories": [
                   {"Code": "14.3.2.0", "Description": "Cultural services (S)"}
               ]}
          ]},
         {"Code": "14.4", "Description": "Education",
          "Subcategories": [
              {"Code": "14.4.1", "Description": "Pre-primary and primary education (S)",
               "Subcategories": [
                   {"Code": "14.4.1.0", "Description": "Pre-primary and primary education (S)"}
               ]},
              {"Code": "14.4.2", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "14.4.2.0", "Description": "Secondary education (S)"}
               ]},
              {"Code": "14.4.3", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "14.4.3.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]},
              {"Code": "14.4.4", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "14.4.4.0", "Description": "Tertiary education (S)"}
               ]},
              {"Code": "14.4.5", "Description": "Education not definable by level (S)",
               "Subcategories": [
                   {"Code": "14.4.5.0", "Description": "Education not definable by level (S)"}
               ]},
              {"Code": "14.4.6", "Description": "Other educational services (S)",
               "Subcategories": [
                   {"Code": "14.4.6.0", "Description": "Other educational services (S)"}
               ]}
          ]},
         {"Code": "14.5", "Description": "Social protection",
          "Subcategories": [
              {"Code": "14.5.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "14.5.0.0", "Description": "Social protection (S)"}
               ]}
          ]},
         {"Code": "14.6", "Description": "Other services",
          "Subcategories": [
              {"Code": "14.6.1", "Description": "Religion (S)",
               "Subcategories": [
                   {"Code": "14.6.1.0", "Description": "Religion (S)"}
               ]},
              {"Code": "14.6.2", "Description": "Political parties, labour, and professional organizations (S)",
               "Subcategories": [
                   {"Code": "14.6.2.0", "Description": "Political parties, labour, and professional organizations (S)"}
               ]},
              {"Code": "14.6.3", "Description": "Environmental protection (S)",
               "Subcategories": [
                   {"Code": "14.6.3.0", "Description": "Environmental protection (S)"}
               ]},
              {"Code": "14.6.4", "Description": "Services n.e.c. (S)",
               "Subcategories": [
                   {"Code": "14.6.4.0", "Description": "Services n.e.c. (S)"}
               ]}
          ]}
     ]}
]
  section_15 = [
    {"Code": "15", "Description": "Individual consumption expenditure of general government",
     "Subcategories": [
         {"Code": "15.1", "Description": "Housing",
          "Subcategories": [
              {"Code": "15.1.0", "Description": "Housing (S)",
               "Subcategories": [
                   {"Code": "15.1.0.0", "Description": "Housing (S)"}
               ]}
          ]},
         {"Code": "15.2", "Description": "Health",
          "Subcategories": [
              {"Code": "15.2.1", "Description": "Pharmaceutical products (ND)",
               "Subcategories": [
                   {"Code": "15.2.1.0", "Description": "Pharmaceutical products (ND)"}
               ]},
              {"Code": "15.2.2", "Description": "Other medical products (ND)",
               "Subcategories": [
                   {"Code": "15.2.2.0", "Description": "Other medical products (ND)"}
               ]},
              {"Code": "15.2.3", "Description": "Therapeutic appliances and equipment (D)",
               "Subcategories": [
                   {"Code": "15.2.3.0", "Description": "Therapeutic appliances and equipment (D)"}
               ]},
              {"Code": "15.2.4", "Description": "Outpatient medical services (S)",
               "Subcategories": [
                   {"Code": "15.2.4.0", "Description": "Outpatient medical services (S)"}
               ]},
              {"Code": "15.2.5", "Description": "Outpatient dental services (S)",
               "Subcategories": [
                   {"Code": "15.2.5.0", "Description": "Outpatient dental services (S)"}
               ]},
              {"Code": "15.2.6", "Description": "Outpatient paramedical services (S)",
               "Subcategories": [
                   {"Code": "15.2.6.0", "Description": "Outpatient paramedical services (S)"}
               ]},
              {"Code": "15.2.7", "Description": "Hospital services (S)",
               "Subcategories": [
                   {"Code": "15.2.7.0", "Description": "Hospital services (S)"}
               ]},
              {"Code": "15.2.8", "Description": "Public health services (S)",
               "Subcategories": [
                   {"Code": "15.2.8.0", "Description": "Public health services (S)"}
               ]}
          ]},
         {"Code": "15.3", "Description": "Recreation and culture",
          "Subcategories": [
              {"Code": "15.3.1", "Description": "Recreational and sporting services (S)",
               "Subcategories": [
                   {"Code": "15.3.1.0", "Description": "Recreational and sporting services (S)"}
               ]},
              {"Code": "15.3.2", "Description": "Cultural services (S)",
               "Subcategories": [
                   {"Code": "15.3.2.0", "Description": "Cultural services (S)"}
               ]}
          ]},
         {"Code": "15.4", "Description": "Education",
          "Subcategories": [
              {"Code": "15.4.1", "Description": "Pre-primary and primary education (S)",
               "Subcategories": [
                   {"Code": "15.4.1.0", "Description": "Pre-primary and primary education (S)"}
               ]},
              {"Code": "15.4.2", "Description": "Secondary education (S)",
               "Subcategories": [
                   {"Code": "15.4.2.0", "Description": "Secondary education (S)"}
               ]},
              {"Code": "15.4.3", "Description": "Post-secondary non-tertiary education (S)",
               "Subcategories": [
                   {"Code": "15.4.3.0", "Description": "Post-secondary non-tertiary education (S)"}
               ]},
              {"Code": "15.4.4", "Description": "Tertiary education (S)",
               "Subcategories": [
                   {"Code": "15.4.4.0", "Description": "Tertiary education (S)"}
               ]},
              {"Code": "15.4.5", "Description": "Education not definable by level (S)",
               "Subcategories": [
                   {"Code": "15.4.5.0", "Description": "Education not definable by level (S)"}
               ]},
              {"Code": "15.4.6", "Description": "Subsidiary services to education (S)",
               "Subcategories": [
                   {"Code": "15.4.6.0", "Description": "Subsidiary services to education (S)"}
               ]}
          ]},
         {"Code": "15.5", "Description": "Social protection",
          "Subcategories": [
              {"Code": "15.5.0", "Description": "Social protection (S)",
               "Subcategories": [
                   {"Code": "15.5.0.0", "Description": "Social protection (S)"}
               ]}
          ]}
     ]}
]

  # Generate a random number between 1 and 15 (inclusive)
  random_number = random.randint(1, 15)
  

 #choose section based on hlsection response 
 # Create a dictionary mapping section codes to the corresponding lists
  section_mapping = {
        1: section_1,
        2: section_2,
        3: section_3,
        4: section_4,
        5: section_5,
        6: section_6,
        7: section_7,
        8: section_8,
        9: section_9,
        10: section_10,
        11: section_11,
        12: section_12,
        13: section_13,
        14: section_14,
        15: section_15,
}
  
  #selecting list
  selected_section = section_mapping.get(random_number)
  

  def select_random_coicop(section_data):
        # Flatten the COICOP hierarchy
        def flatten(categories):
            for category in categories:
                yield category
                if "Subcategories" in category:
                    yield from flatten(category["Subcategories"])

        # Get all COICOP codes
        all_coicop_codes = [(node["Code"], node["Description"]) for node in flatten(section_data)]

        # Filter codes with three decimal points
        low_level_coicop_codes = [(code, desc) for code, desc in all_coicop_codes if len(code.split(".")) == 4]

        # Select a random code
        if low_level_coicop_codes:
            return random.choice(low_level_coicop_codes)
        else:
            return None  # Return None if no low-level codes found

  # Randomly select a low-level COICOP code from Section 15
  random_coicop_code = select_random_coicop(selected_section)
  print (random_coicop_code)
  print (type(random_coicop_code))
  
  

findNextCompany()  





