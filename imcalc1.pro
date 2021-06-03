pro imcalc1,nim1,nim2

;  imcalc moo3 moo4 'if im1 .gt. 800 then 1 else 0'

  im1=readfits(nim1)
  ind=where(im1 gt 800)
  outim=im1-im1
  outim(ind)=1
  writefits,nim2,outim

end

  
