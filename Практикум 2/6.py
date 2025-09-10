weight=int(input())
height=int(input())
weight_kg=weight*0.453592
height_m=height*0.0254
IMT=(weight_kg/(height_m**2))
ans=round(IMT,2)
print(ans)