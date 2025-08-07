-- 1. Count total records
SELECT COUNT(*) AS total_records FROM 'beneficiaries.csv';

-- 2. Count by StateCode
SELECT StateCode, COUNT(*) AS count FROM 'beneficiaries.csv' GROUP BY StateCode;

-- 3. Count by RoutingIdentifierType
SELECT RoutingIdentifierType, COUNT(*) AS count FROM 'beneficiaries.csv' GROUP BY RoutingIdentifierType;

-- 4. List unique cities
SELECT DISTINCT City FROM 'beneficiaries.csv';

-- 5. Show sample records
SELECT * FROM 'beneficiaries.csv' LIMIT 5;
