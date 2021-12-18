```python
def solve(COST):
    w, h = COST.shape
    open = [(0, 0, 0)]
    q.heapify(open)
    mins = sys.maxsize * np.ones(COST.shape, dtype=int)
     mins[0, 0] = 0
      end = w-1, h-1

       while open:
            curcost, x, y = q.heappop(open)
            if (x, y) == end:
                break

            for xoff, yoff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neigh = (x+xoff, y+yoff)
                if 0 > neigh[0] or neigh[0] >= w or 0 > neigh[1] or neigh[1] >= h:
                    continue

                xcost = COST[neigh] + curcost
                if xcost < mins[neigh]:
                    mins[neigh] = xcost
                    q.heappush(open, (mins[neigh], *neigh))

        return mins[end]


def D():
  while True:
     d, p = heappop(dist)
     vis[p] = 1
     

     neighbours = [p+w] * (p < h*w-w) + [p-w] * (p >= w) + [p+1] * ((p+1) % w) + [p-1] * (p % w)  
     for np in neighbours:
       if not vis[np]:
         alt = d + data[np]
         if np == h*w-1:
            return alt
        
         if alt < ardist[np]:              
            ardist[np] = alt
            heappush(dist, (alt,np))
           
```