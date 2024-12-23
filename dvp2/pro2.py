def ceate_gml(filename):
    gml_content = """graph [
    directed 1
    node [
    id 1
    lablel "node 1" 
    ]
    node [
    id 2
    lablel "node 2" 
    ]

    edge[
    source 1
    target 2
    
    ]
    
]"""

    with open(filename, 'w') as file:
        file.write(gml_content)

ceate_gml("charan.gml")
