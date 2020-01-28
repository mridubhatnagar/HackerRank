

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