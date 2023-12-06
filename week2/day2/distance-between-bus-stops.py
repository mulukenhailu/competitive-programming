class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#          1 3
#         123456
#         f=2+3=5==>start+3=[start:destination]
#         b=1+6+5+4=16==>[0:start]+[destination:]
        
#             1   3
#         [3,14,5,2,21,12,17,24,11,16,15,4,9]
#         f=5+14=19=[start-1:destination-1:-1]
#         b=2+21+12+17+24+11+16+15+4+9+3=[destination-1::-1]+[start:]

        print(len(distance))

        if start<destination:
            f= sum(distance[start:destination]) 
            b=sum(distance[0:start]+distance[destination:])
            
            print(distance[start:destination])
            print(distance[0:start]+distance[destination:])
            return min(f, b)
        else:
            if destination!=0:
                f=sum(distance[start-1:destination-1:-1])
                b=sum(distance[destination-1::-1]+distance[start:])
#               print(distance[start-1::-1])
            else:
                f=sum(distance[start-1::-1])
                b=sum(distance[start:])
                print(distance[start-1:destination-1:-1])
                
            
            return min(f, b)
