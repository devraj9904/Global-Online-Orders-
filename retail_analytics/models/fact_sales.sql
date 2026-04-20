SELECT
    od.orderdetailid,
    od.orderid,
    od.productid,
    o.customerid,
    o.employeeid,
    o.shipperid,
    o.orderdate,
    od.quantity,
    p.price AS unit_price, 
    (od.quantity * p.price) AS totalamount
FROM public.ordersdetails od
JOIN public.orders o ON od.orderid = o.orderid
JOIN public.products p ON od.productid = p.productid