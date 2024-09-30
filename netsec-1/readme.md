# Network Security - HTTP Mayhem

มี http ขอสองไฟล์ ก็ export object -> http ออกมาให้หมด

![alt](1.png)

พอไปแปะใน llm มันบอกว่า `ฝัง flag ลงในภาพโดยการปรับบิตที่มีนัยสำคัญน้อยที่สุด (the least significant bit : LSB) ของแต่ละพิกเซล` งั้นลองให้มันเขียน reverse lsb ออกมา

![alt](2.png)

พอรันดูก็จะเห็นว่า flag ไม่ออก

![alt](3.png)

งั้นลองไล่ดูทีละสีดิ

![alt](4.png)

ได้มาแล้วว THCTT24{82d27383f4ce66b375cfc48b60afcb30}

[Index](../)
