import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';
import 'navigation.dart';

class MyLoginPage extends StatefulWidget {
  MyLoginPage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyLoginPageState createState() => _MyLoginPageState();
}

class _MyLoginPageState extends State<MyLoginPage> {
  final myLoginController = TextEditingController();
  final myPasswordController = TextEditingController();
  bool connexion = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MIAGED'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            TextFormField(
              controller: myLoginController,
              decoration: const InputDecoration(
                  labelText: 'Login',
                  border: OutlineInputBorder()),
              validator: (value1) {
                if (value1.isEmpty) {
                  return 'Please enter your login';
                }
                return null;
              },
            ),
            TextFormField(
              controller: myPasswordController,
              decoration: const InputDecoration(
                  labelText: 'Password',
                  border: OutlineInputBorder()),
              obscureText: true,
              validator: (value2) {
                if (value2.isEmpty) {
                  return 'Please enter your password';
                }
                return null;
              },
            ),
            FlatButton(
              color: Colors.grey,
              onPressed: () {
                database(myLoginController.text, myPasswordController.text);
              },
              child: Text(
                "Connect",
              ),
            )
          ],
        ),
      ),
    );
  }

  void database(String user, String pwd) async{
    Session sess = new Session();
    FirebaseFirestore.instance.collection('logins').get().then((QuerySnapshot querySnapshot) {
      querySnapshot.docs.forEach((doc) {
        if(doc["login"] == user){
          if(doc["password"] == pwd){
            connexion = true;
            sess.id =  doc.id;
            sess.login = user;
            sess.password = pwd;
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => MyNavigationPage()),
            );
          } else {
            connexion = false;
          }
        }
      });
    });
  }
}