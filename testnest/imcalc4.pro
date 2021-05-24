pro imcalc4,nim1,nim2,nim3

  ;imcalc foo2m,foo2a foo2a1 'if im1 .gt. 777777 .and. im2 .lt. 777777 then im2 else im1'

  im1=readfits(nim1)
  im2=readfits(nim2)
  im3=im1
  ind=where(im1 gt 777777 and im2 lt 777777)  
  im3(ind)=im2(ind)

  writefits,nim3,im3 
end
