pro imcalc3,nim1,nim2,nim3

  ;imcalc foo2,mask_0008_im1final foo2m 'if im2 .eq. 0 then im1 else 999999'

  im1=readfits(nim1)
  im2=readfits(nim2)
  ind=where(abs(im2) gt 1e-6)
  im3=im1
  im3(ind)=999999

  writefits,nim3,im3

 end


  
