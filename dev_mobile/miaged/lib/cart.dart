import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';
import 'shop.dart';

class MyCart extends StatefulWidget {
  MyCart({Key key}) : super(key: key);

  @override
  _MyCartState createState() => _MyCartState();
}

class _MyCartState extends State<MyCart> {
  _MyCartState();

  @override
  Widget build(BuildContext context) {
    getCart();
    var ccount = 0;
    var total = 0;
    if(cartL !=  null){
      ccount = cartL.length;
    }
    for(int x=0; x<ccount; x++){
      total += int.parse(cartL[x].price);
    }
    const Key centerKey = ValueKey('bottom-sliver-list');
    return Scaffold(
        floatingActionButton: FloatingActionButton.extended(
          label: Text("Total : $total"),
        ),
      body: Container(
        child: CustomScrollView(
          center: centerKey,
          slivers: <Widget>[
            SliverList(
              key: centerKey,
              delegate: SliverChildBuilderDelegate((BuildContext context,int index) {
                return Row(
                  children: <Widget>[
                    Column(
                      children: [
                        Image(
                          image: NetworkImage(cartL[index].link),
                          width: 100,
                        ),
                      ],
                    ),
                    Column(
                      children: <Widget>[
                        Text('Title  : '+cartL[index].title),
                        Text('Size   : '+cartL[index].size),
                        Text('Price  : '+cartL[index].price),
                      ],
                    ),
                    Column(
                      children: [
                        IconButton(
                          icon: Icon(Icons.delete),
                          onPressed: (){
                            FirebaseFirestore.instance.collection('logins/'+session.id+'/panier').doc(cartL[index].id).delete();
                          },
                        ),
                      ],
                    )
                  ],
                );
              },
                childCount: ccount,
              ),
            ),
          ],
        ),
      )
    );
  }
  void getCart() {
    List<Item> cart = [];
    FirebaseFirestore.instance.collection('logins/'+session.id+'/panier').get().then((QuerySnapshot querySnapshot) {
      querySnapshot.docs.forEach((doc) {
        Item item = new Item();
        item.id = doc.id;
        item.title = doc["title"];
        item.price = doc["price"];
        item.brand = doc["brand"];
        item.size = doc["size"];
        item.link = doc["link"];
        cart.add(item);
      });
      cartL = cart;
      setState(() {
        _MyCartState();
      });
    });
  }
}
