# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.insert(0,0);
    stops.append(distance);

    retanqueados=0;tanqueActual=0;ultimaTanqueada = 0;
    while(stops[tanqueActual] < distance):
        ultimaTanqueada = tanqueActual;
        while stops[tanqueActual] < distance and stops[tanqueActual+1]-stops[ultimaTanqueada] <= tank :
            tanqueActual+=1;
        if ultimaTanqueada == tanqueActual:
            return -1
        if stops[tanqueActual] < distance:
            retanqueados+=1;
    return retanqueados;
    

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))