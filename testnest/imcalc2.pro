pro imcalc2,nim1,nim2,nim3

;imcalc moo3,moo5 mask_0008_im1final.fits 'if im1 .gt. 200 .and. im2 .gt. 0.001 then 1 else 0'  im1=readfits(nim1)

  im1=readfits(nim1)
  im2=readfits(nim2)
  ind=where(im1 gt 200 and im2 gt 0.001)
  im3=im1-im1
  im3(ind)=1

  writefits,nim3,im3

 end


  
