import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:miaged/navigation.dart';
import 'main.dart';
import 'shop.dart';

class MyItemDetails extends StatefulWidget {
  MyItemDetails({Key key}) : super(key: key);
  @override
  _MyItemDetailsState createState() => _MyItemDetailsState();
}

class _MyItemDetailsState extends State<MyItemDetails> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MIAGED'),
      ),
      body: Row(
          children: <Widget>[
            Column(
              children: [
                Image(
                  image: NetworkImage(itemsL[currItem].link),
                  width: 100,
                ),
              ],
            ),
            Column(
              children:<Widget>[
                Text('Title  : '+itemsL[currItem].title),
                Text('Size   : '+itemsL[currItem].size),
                Text('Price  : '+itemsL[currItem].price),
              ],
            ),
            Column(
              children: [
                FlatButton(
                  color: Colors.grey,
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => MyNavigationPage()),
                    );
                  },
                  child: Text(
                    "Back",
                  ),
                ),
                FlatButton(
                  color: Colors.grey,
                  onPressed: () {
                    FirebaseFirestore.instance.collection('logins').doc(session.id).collection('panier').add({
                      'id': itemsL[currItem].id,
                      'title': itemsL[currItem].title,
                      'price': itemsL[currItem].price,
                      'brand': itemsL[currItem].brand,
                      'size': itemsL[currItem].size,
                      'link': itemsL[currItem].link,});
                  },
                  child: Text(
                    "Add to cart",
                  ),
                )
              ],
            )
          ],
      ),
    );
  }
}