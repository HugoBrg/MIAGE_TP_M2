import 'package:flutter/material.dart';

import 'itemDetails.dart';
import 'shop.dart';
import 'login.dart';
import 'cart.dart';
import 'navigation.dart';
import 'profile.dart';

import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MIAGED',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyLoginPage(),
      //home: MyNavigationPage(),
      //home: MyItemDetails(),
    );
  }
}

class Session {
  static final Session sess = new Session._internal();
  String id;
  String login;
  String password;
  factory Session() {
    return sess;
  }
  Session._internal();
}

final session = Session();
List<Item> itemsL = [];
List<Item> cartL = [];
int total = 0;
int currItem;


