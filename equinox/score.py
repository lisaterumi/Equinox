#COPYRIGHT Justin A. Gould

#Required Packages
import pandas as pd

#Fleiss's Kappa
def fleiss_kappa(entities, num_annotators, master, na=False):
    entities = __entities
    if (na) & ("NA" not in _entities):
        _entities.extend(["NA"]) #Not Annotated Class
    
    #Calculate P_c per entity
    P_c_values = []
    for entity in _entities:
        #Get Sum of Entity Values (Column)
        _sum = sum(master[entity])

        #Get Number of Entries
        _num_entries = len(master)

        #Calculate P_c
        P_c = (_sum) / (_num_entries * num_annotators)
        P_c_values.append(P_c)
        
    #Calculate P_i per Document
    P_i_values = []
    for index, row in master.loc[:, _entities[0]:_entities[-1]].iterrows():
        #Loop Through Entities
        _squares = []
        for entity in _entities:
            #Get Square of Annotation Count
            _square = row[entity]**2
            _squares.append(_square)

        #P_i
        P_i = ((sum(_squares)) - num_annotators) / (num_annotators * (num_annotators - 1))
        P_i_values.append(P_i)
    
    #Calculate P
    P = sum(P_i_values) / len(master)
    
    #Calculate P_e
    P_e = sum([(lambda x: x**2)(x) for x in P_c_values])
    
    #Calculate k
    k = (P - P_e) / (1 - P_e)
    
    return k