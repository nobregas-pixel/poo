from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO cliente (nome, email, fone, senha, foto)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_foto()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM cliente"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Cliente(id, nome, email, fone, senha, foto) for (id, nome, email, fone, senha, foto) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM cliente WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Cliente(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE cliente SET nome=?, email=?, fone=?, senha=?, foto=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_foto(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM cliente WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()