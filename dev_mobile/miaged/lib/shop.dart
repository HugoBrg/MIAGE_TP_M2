import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:miaged/itemDetails.dart';
import 'main.dart';

class MyShop extends StatefulWidget {
  MyShop({Key key}) : super(key: key);

  @override
  _MyShopState createState() => _MyShopState();
}

class _MyShopState extends State<MyShop> {
  _MyShopState();

  @override
  Widget build(BuildContext context) {
    getItems();
    var ccount = 0;
    if(itemsL !=  null){
      ccount = itemsL.length;
    }
    const Key centerKey = ValueKey('bottom-sliver-list');
    return Scaffold(
      body: CustomScrollView(
        center: centerKey,
        slivers: <Widget>[
          SliverList(
            key: centerKey,
            delegate: SliverChildBuilderDelegate((BuildContext context, int index) {
              return InkWell(
                child: Container(
                  alignment: Alignment.center,
                  height: 200,
                  child: Text('Title:${itemsL[index].title} Size : ${itemsL[index].size} Price ${itemsL[index].price}',
                    style: TextStyle(
                      fontSize: 16,
                      foreground: Paint()
                        ..style = PaintingStyle.stroke
                        ..strokeWidth = 1
                        ..color = Colors.blue[700],
                    ),),
                  decoration: BoxDecoration(
                    image: DecorationImage(
                      image: NetworkImage(itemsL[index].link),
                    ),
                  ),
                ),
                onTap: () {
                  currItem = index;
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => MyItemDetails()),
                  );
                },
              );
            },
              childCount: ccount,
            ),
          ),
        ],
      ),
    );
  }
  void getItems() {
    List<Item> items = [];
    FirebaseFirestore.instance.collection('shop').get().then((QuerySnapshot querySnapshot) {
      querySnapshot.docs.forEach((doc) {
        Item item = new Item();
        item.id = doc.id;
        item.title = doc["title"];
        item.price = doc["price"];
        item.brand = doc["brand"];
        item.size = doc["size"];
        item.link = doc["link"];
        items.add(item);
      });
      itemsL = items;
      setState(() {
        _MyShopState();
      });
    });
  }
}


class Item {
  String id;
  String title;
  String price;
  String brand;
  String size;
  String link;
  Item();
}
