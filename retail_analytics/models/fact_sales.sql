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
FROM public.ordersdetails AS od
INNER JOIN public.orders AS o ON od.orderid = o.orderid
INNER JOIN public.products AS p ON od.productid = p.productid
