SELECT
    p.productid,
    p.productname,
    p.price AS currentprice,
    c.categoryname,
    c.description AS categorydescription,
    s.suppliername,
    s.country AS suppliercountry
FROM public.products AS p
LEFT JOIN public.categories AS c ON p.categoryid = c.categoryid
LEFT JOIN public.suppliers AS s ON p.supplierid = s.supplierid
