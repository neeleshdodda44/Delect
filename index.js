function RegisterController($scope,$http){
  $scope.details=[                {'firstname':"Ex: Burritos", 'id': 0}
  ];

  $scope.foodList=[];
  
  $scope.adddetails=function(){
<<<<<<< HEAD
    $scope.details.push({'firstname':$scope.firstname, 'id':$scope.details.length})
    $scope.foodString.push($scope.firstname);
=======
    
 $scope.details.push({'firstname':$scope.firstname, 'id':$scope.details.length})
>>>>>>> f3226fb9f69b39ec09d1570b1e907475a9114485
    $scope.firstname="";
    // $scope.foodString = $scope.foodString + $scope.firstname + ",";
    $scope.frm.$setPristine();
  }
  
  $scope.deletedetail=function(index){
     $scope.details.splice(index,1);
    $("#del").fadeOut(2000);
  };

   $scope.submit=function(){
 // $scope.details.push({'firstname':$scope.firstname, 'id':$scope.details.length})
 //    $scope.firstname="";
    
 //    $scope.frm.$setPristine();
  }
  
  $scope.tickcross={};
  
  for (var i = 0, length = $scope.details.length; i < length; i++) {
      $scope.tickcross[$scope.details[i].id] = false;
    }
  
  //$scope.tickcross=false;
  
  $scope.modify=function(data){     
      //$scope.tickcross=true;
      $scope.tickcross[data.id]=true;
      console.log(data)
  }
  
  $scope.update=function(data){
     // $scope.tickcross=false;    
      $scope.tickcross[data.id]=false;          
  }
  
}