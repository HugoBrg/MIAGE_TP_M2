import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'login.dart';
import  'main.dart';

class MyProfilePage extends StatefulWidget {
  MyProfilePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyProfilePageState createState() => _MyProfilePageState();
}

class _MyProfilePageState extends State<MyProfilePage> {
  final myLoginController = TextEditingController();
  final myPasswordController = TextEditingController();
  final myBirthdateController = TextEditingController();
  final myAdressController = TextEditingController();
  final myPostalcodeController = TextEditingController();
  final myCityController = TextEditingController();

  bool connexion = false;

  @override
  Widget build(BuildContext context) {
    getProfile();
    return Scaffold(
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            children: <Widget>[
              Text("Login"),
              TextFormField(
                enabled: false,
                decoration: InputDecoration(
                    labelText: prof.login,
                    border: OutlineInputBorder()),
              ),
              Text("Password"),
              TextFormField(
                controller: myPasswordController,
                decoration: InputDecoration(
                    labelText: "Type your password",
                    border: OutlineInputBorder()),
                obscureText: true,
                validator: (value2) {
                  if (value2.isEmpty) {
                    return 'Please enter your password';
                  }
                  return null;
                },
              ),
              Text("Birthdate"),
              TextFormField(
                controller: myBirthdateController,
                decoration: InputDecoration(
                    labelText: prof.birthdate,
                    border: OutlineInputBorder()),
              ),
              Text("Adress"),
              TextFormField(
                controller: myAdressController,
                decoration: InputDecoration(
                    labelText: prof.adress,
                    border: OutlineInputBorder()),
              ),
              Text("Postal Code"),
              TextFormField(
                controller: myPostalcodeController,
                decoration: InputDecoration(
                    labelText: prof.postalcode,
                    border: OutlineInputBorder()),
              ),
              Text("City"),
              TextFormField(
                controller: myCityController,
                decoration: InputDecoration(
                    labelText: prof.city,
                    border: OutlineInputBorder()),
              ),
              FlatButton(
                color: Colors.grey,
                onPressed: () {
                  FirebaseFirestore.instance.collection('logins').doc(session.id).update({
                    'birthdate': myBirthdateController.text,
                    'adress': myAdressController.text,
                    'postalcode': myPostalcodeController.text,
                    'city': myCityController.text,
                  });
                },
                child: Text(
                  "Validate",
                ),
              ),
              FlatButton(
                color: Colors.grey,
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => MyLoginPage()),
                  );
                },
                child: Text(
                  "Deconnect",
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  void getProfile() async{
    FirebaseFirestore.instance.collection('logins').get().then((QuerySnapshot querySnapshot) {
      querySnapshot.docs.forEach((doc) {
        if(doc["login"] == session.login) {
          if (doc["password"] == session.password) {
            prof.id = doc.id;
            prof.login = doc["login"];
            prof.password = doc["password"];
            prof.birthdate = doc["birthdate"];
            prof.adress = doc["adress"];
            prof.postalcode = doc["postalcode"];
            prof.city = doc["city"];
          }
        }
      });
      setState(() {
        _MyProfilePageState();
      });
    });
  }

}

class Profile {
  String id;
  String login;
  String password;
  String birthdate;
  String adress;
  String postalcode;
  String city;
}

Profile prof = new Profile();