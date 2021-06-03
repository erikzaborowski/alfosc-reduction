pro imxcorr
  plotit=0
  im1=readfits('trace1.fits')
  im2=readfits('trace2.fits')
  c=c_correlate(im1(240:2000,500),im2(240:2000,500),findgen(401)-200)
  if(plotit)then plot,findgen(401)-200,c,psym=10
  qui=where(abs(c-max(c)) lt 1e-6)
  x=findgen(401)-200
  dx=total(x(qui))/n_elements(qui)

  close,1
  openw,1,'tempcl1'
  printf,1,'imshift hoo4 hoo6 '+string(-1*dx)+' 0'
  close,1
  close,1
  openw,1,'tempcl2'
  printf,1,'imshift diff1 diff2 '+string(-1*dx)+' 0'
  close,1
    
end

pro maskxcorr,nim1,nim2

plotit=0
  
im=readfits(nim1)
imtrace=im(240:2000,500)-median(reform(im(240:2000,500)),151)
qui=where(abs(imtrace) ge 1e-6)
h=histogram(imtrace(qui),binsize=0.5,min=-15,max=45)
hx=findgen(n_elements(h))*0.5-15+0.25
if(plotit)then !p.multi=[0,1,2]
if(plotit)then plot,hx,h,psym=10
yf=gaussfit(hx,h,g,nterm=3)
if(plotit)then oplot,hx,yf,col=255
qui=where(hx lt g(1)+2*g(2))
yf=gaussfit(hx(qui),h(qui),g,nterm=3)
if(plotit)then oplot,hx(qui),yf,col=255,thick=3
qui=where(imtrace gt g(1)+3*g(2))
if(plotit)then plot,imtrace
mask=im(*,500)-im(*,500)
mask1=mask(240:2000)
mask1(qui)=1.0
mask2=smooth(mask1,5)
qui=where(mask2 gt 0.001)
mask1(qui)=1.0
mask(240:2000)=mask1
if(plotit)then oplot,qui,imtrace(qui),psym=2,col=255
allmask=im-im
s=size(allmask)
for i=0,s(2)-1 do allmask(*,i)=mask
writefits,nim2,allmask

end
