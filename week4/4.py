import json
#1
def jsonn(f):
    with open(f,'r') as file:
        data=json.load(f)
    
    print("interface status")
    print("=" *80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
    print("-" * 80)

    for i in data['imdata']:
        attributes = i['l1PhysIf']['attributes']
        dn = attributes['dn']
        descr = attributes.get('descr', '')
        speed = attributes['speed']
        mtu = attributes['mtu']
        print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")

jsonn('sample.py')       