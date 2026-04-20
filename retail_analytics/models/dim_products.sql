SELECT
    p.productid,
    p.productname,
    p.price AS currentprice,
    c.categoryname,
    c.description AS categorydescription,
    s.suppliername AS suppliername,
    s.country AS suppliercountry
FROM public.products p
LEFT JOIN public.categories c ON p.categoryid = c.categoryid
LEFT JOIN public.suppliers s ON p.supplierid = s.supplierid