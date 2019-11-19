import 'whatwg-fetch';

export const courseServices = {
    viewAssignments,
    submitAssignments,
    gradeAssignment,
    viewAssignmentGrades,
    createAssignment,
    takeAttendance,
    viewAttendance,
    uploadMaterial,
    searchMaterial,
    deleteMaterial,
    plagiarismCheck
}

const courseendpoints = {
    viewAssignments: 'http://192.168.1.207:5001/csm/assignments/view/',
    submitAssignments: 'http://192.168.1.207:5001/csm/assignments/submit',
    gradeAssignment: 'http://192.168.1.207:5001/csm/assignments/gradeAssignment',
    viewAssignmentGrades: 'http://192.168.1.207:5001/csm/assignments/viewgrades/',
    createAssignment: 'http://192.168.1.207:5001/csm/assignments/create',
    takeAttendance: 'http://192.168.1.207:5001/csm/attendance/takeAttendance',
    viewAttendance: 'http://192.168.1.207:5001/csm/attendance/viewAttendance/',
    uploadMaterial: 'http://192.168.1.207:5001/csm/studymaterial/uploadMaterial',
    searchMaterial: 'http://192.168.1.207:5001/csm/studymaterial/search/',
    deleteMaterial: 'http://192.168.1.207:5001/csm/studymaterial/delete/',
    plagiarismCheck: 'http://192.168.1.207:5001/csm/assignments/plagiarismCheck'
};


// courseId is string
function viewAssignments(courseId, token) {
    return fetch(courseendpoints.viewAssignments+courseId+'?token='+token);
}

//s_assignment object which contains : studentName, studentId, filename, a_id
function submitAssignments(s_assignment, token) {
    return fetch(courseendpoints.submitAssignments+'?token='+token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(s_assignment),
    });
}

//g_assignment object which contains : a_id, filename
function gradeAssignment(g_assignment, token){
    return fetch(courseendpoints.gradeAssignment+'?token='+token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(g_assignment),
    });
}

function viewAssignmentGrades(studentId, token){
    return fetch(courseendpoints.viewAssignmentGrades+studentId+'?token='+token);
}

//c_assignment object which contains : course_id, a_id, ques, exp, deadline, document
function createAssignment(c_assignment, token){
    return fetch(courseendpoints.createAssignment+'?token='+token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(c_assignment),
    });
}

//attendance object which contains : c_id, s_list, hrs
function takeAttendance(attendance, token){
    return fetch(courseendpoints.takeAttendance+'?token='+token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(attendance),
    });
}

function viewAttendance(s_id, token){
    return fetch(courseendpoints.viewAttendance+s_id+'?token='+token);
}

//material object which contains : course_id, desc, title, material
function uploadMaterial(material, token){
    return fetch(courseendpoints.uploadMaterial+'?token='+token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(material),
    });
}

function searchMaterial(course_id, token){
    return fetch(courseendpoints.searchMaterial+course_id+'?token='+token);
}

function deleteMaterial(mId, token){
    return fetch(courseendpoints.deleteMaterial+mId+'?token='+token, {
        method: 'DELETE',
    });
}

function plagiarismCheck(assignId, token){
    return fetch(courseendpoints.plagiarismCheck+assignId+'?token='+token);
}