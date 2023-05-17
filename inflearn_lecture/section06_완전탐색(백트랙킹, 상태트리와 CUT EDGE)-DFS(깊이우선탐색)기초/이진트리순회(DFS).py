def dfs_preorder(vertex):
    print(vertex)  # 함수 본연의 일
    dfs_preorder(vertex * 2)  # left child
    dfs_preorder(vertex * 2 + 1)  # right child


def dfs_inorder(vertex):
    dfs_preorder(vertex * 2)
    print(vertex)  # 함수 본연의 일
    dfs_preorder(vertex * 2 + 1)


def dfs_postorder(vertex):
    dfs_preorder(vertex * 2)
    dfs_preorder(vertex * 2 + 1)
    print(vertex)  # 함수 본연의 일


if __name__ == "__main__":
    dfs_preorder()

