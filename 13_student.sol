// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDatabase {
    struct Student {
        string name;
        uint256 rollNumber;
        string studentClass;
    }

    Student[] private students;

    function addStudent(string memory name, uint256 rollNumber, string memory studentClass) public {
        students.push(Student(name, rollNumber, studentClass));
    }

    function getStudentByID(uint256 ID) public view returns (string memory, uint256, string memory) {
        require(ID < students.length, "Student does not exist in database");
        Student storage s = students[ID];
        return (s.name, s.rollNumber, s.studentClass);
    }

    function getTotalNumberOfStudents() public view returns (uint256) {
        return students.length;
}
}

