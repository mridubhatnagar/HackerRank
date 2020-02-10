

1. -- https://www.hackerrank.com/challenges/revising-the-select-query/problem
select * from city where population > 100000 and countrycode='USA';

2. -- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
select name from city where population>120000 and countrycode='USA';

3. -- https://www.hackerrank.com/challenges/select-all-sql/problem
select * from city;

4. --https://www.hackerrank.com/challenges/select-by-id/problem
select * from city where id='1661';

5. --https://www.hackerrank.com/challenges/japanese-cities-attributes/problem
select * from city where countrycode='JPN';

6. --https://www.hackerrank.com/challenges/japanese-cities-name/problem
select name from city where countrycode='JPN';

7. --https://www.hackerrank.com/challenges/weather-observation-station-1/problem
select city, state from station;

8. --https://www.hackerrank.com/challenges/weather-observation-station-3/problem
select distinct city from station where id % 2=0;

9. --https://www.hackerrank.com/challenges/name-of-employees/problem
select name from Employee order by name asc;

10. --https://www.hackerrank.com/challenges/salary-of-employees/problem
select name from employee where salary>2000 and months < 10 order by employee_id asc;

11. --https://www.hackerrank.com/challenges/weather-observation-station-6/problem
select distinct city from station where city REGEXP '^[aeiou]';

12. --https://www.hackerrank.com/challenges/weather-observation-station-7/problem
select distinct city from station where city REGEXP '[aeiou]$';

13. --https://www.hackerrank.com/challenges/weather-observation-station-9/problem
select distinct city from station where city REGEXP '^[^aeiou]';

14. --https://www.hackerrank.com/challenges/weather-observation-station-10/problem
select distinct city from station where city REGEXP '[^aeiou]$';

15. --https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
select count(*) from city where population > 100000;

16. --https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
select sum(population) from city where district='California';

17. --https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
select avg(population) from city where district='California';

18. --https://www.hackerrank.com/challenges/japan-population/problem
select sum(population) from city where countrycode='JPN';

19. --https://www.hackerrank.com/challenges/population-density-difference/problem
select max(population) - min(population) from city;

20. --https://www.hackerrank.com/challenges/earnings-of-employees/problem
select (months*salary) as earnings, count(*) from employee group by 1 order by 1 desc LIMIT 1;

21. --https://www.hackerrank.com/challenges/weather-observation-station-2/problem
select round(sum(LAT_N), 2), round(sum(LONG_W),2) from station;

22. --https://www.hackerrank.com/challenges/weather-observation-station-13/problem
select round(sum(LAT_N),4) from station where LAT_N>38.7880 and LAT_N<137.235;

23. --https://www.hackerrank.com/challenges/weather-observation-station-14/problem
select round(max(LAT_N),4) from station where LAT_N < 137.2345;

24. --https://www.hackerrank.com/challenges/average-population/problem
select round(avg(population)) from city;

25. -- https://www.hackerrank.com/challenges/weather-observation-station-16/problem
select round(min(LAT_N), 4) from station where LAT_N > 38.7780;

26. -- https://www.hackerrank.com/challenges/asian-population/problem
select sum(city.population) from city inner join country on city.countrycode=country.code where continent='Asia';

27. --https://www.hackerrank.com/challenges/african-cities/problem
select city.name from city inner join country on city.countrycode=country.code where continent='Africa';

28. --https://www.hackerrank.com/challenges/weather-observation-station-4/problem
select count(city)-count(distinct city) from station;

29. --https://www.hackerrank.com/challenges/weather-observation-station-8/problem
select city from station where city REGEXP '^[aeiou].*[aeiou]$';

30. --https://www.hackerrank.com/challenges/weather-observation-station-11/problem
select distinct city from station where city REGEXP '^[^aeiou]|[^aeiou]$';

31. --https://www.hackerrank.com/challenges/weather-observation-station-12/problem
select distinct city from station where city REGEXP '^[^aeiou].*[^aeiou]$';

32. --https://leetcode.com/problems/combine-two-tables/
select FirstName, LastName, City, State from Person left join Address on Person.PersonId=Address.PersonId 